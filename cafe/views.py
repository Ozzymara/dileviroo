from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.contrib import messages
from cafe.models import *
from django.core.files.storage import FileSystemStorage
from datetime import date, datetime, timedelta
import json
import ast

from itertools import groupby
from django.db.models import Sum
from .models import Order, User, Rating
from .forms import ReviewForm, DeleteConfirmForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.http import HttpResponse

User = get_user_model()

context = {}


def menu(request):
    """
    Display the restaurant menu organized by categories.

    Retrieves all menu items from the database, groups them by category,
    and renders them in the menu template.

    Args:
        request (HttpRequest): The HTTP request object

    Returns:
        HttpResponse: Rendered menu.html template with categorized menu items

    Context:
        items_by_category (dict): Menu items grouped by category
    """
    # Get all menu items with images, ordered by list_order for custom ordering
    menu_items = MenuItem.objects.filter(pic__isnull=False).exclude(
        pic='').order_by('list_order', 'price', 'name')
    items_by_category = {}

    # Group menu items by category for organized display
    for key, group in groupby(menu_items, key=lambda x: x.category):
        items_by_category[key] = list(group)

    context = {'items_by_category': items_by_category}
    return render(request, 'menu.html', context)


def all_orders(request):
    """
    Display all orders in the system grouped by table number.

    Retrieves all orders from the database, groups them by table,
    and parses the JSON items data for display. Used by staff to view
    all current orders.

    Args:
        request (HttpRequest): The HTTP request object

    Returns:
        HttpResponse: Rendered all_orders.html template with orders by table

    Context:
        order_by_table (dict): Orders grouped by table number

    Note:
        Handles JSON parsing errors gracefully by setting empty dict fallback
    """
    context = {}
    # Get all orders sorted by most recent first
    orders = Order.objects.all().order_by('-order_time')
    order_by_table = {}

    # Group orders by table number for organized display
    for key, group in groupby(orders, key=lambda x: x.table):
        order_by_table[key] = list(group)

    # Parse JSON data for each order with error handling
    for table, orders in order_by_table.items():
        for ord in orders:
            items_json_str = ord.items_json
            try:
                ord.items_json = json.loads(items_json_str)
            except (json.JSONDecodeError, TypeError, ValueError):
                ord.items_json = {}
                # Log parsing error for debugging
                print(
                    f"⚠️ JSONDecodeError for order {ord.id}: {items_json_str}")

    context = {'order_by_table': order_by_table}

    return render(request, 'all_orders.html', context)


def offers(request):
    """
    Display the offers/promotions page.

    Args:
        request (HttpRequest): The HTTP request object

    Returns:
        HttpResponse: Rendered offers.html template
    """
    return render(request, 'offers.html')


def reviews(request):
    """
    Handle customer reviews display and submission with CRUD functionality.

    GET: Displays all customer reviews ordered by date (newest first) with edit/delete buttons  # noqa: E501
    POST: Processes new review submission from authenticated users

    Args:
        request (HttpRequest): The HTTP request object

    Returns:
        HttpResponse: Rendered reviews.html template with all reviews and CRUD buttons

    Context:
        reviews (QuerySet): All reviews ordered by date descending
        show_crud_buttons (bool): Whether to show edit/delete buttons for authenticated users

    Note:
        Edit/delete buttons are only visible to authenticated users
        Uses Post-Redirect-Get pattern to prevent duplicate submissions on refresh
    """
    if request.method == 'POST':
        # Extract user information for review
        fname = request.user.first_name
        lname = request.user.last_name
        cmt = request.POST.get('comment')
        datetime_now = datetime.now()

        # Create and save new review
        review = Rating(name=fname + ' ' + lname,
                        comment=cmt,
                        r_date=datetime_now)
        review.save()
        messages.success(
            request, 'Your review has been submitted successfully!')

        # Redirect to prevent duplicate submission on refresh (PRG pattern)
        return redirect('reviews')

    # Get all reviews ordered by newest first
    all_reviews = Rating.objects.all().order_by('-r_date')
    context = {
        'reviews': all_reviews,
        'show_crud_buttons': request.user.is_authenticated,
        'user_authenticated': request.user.is_authenticated
    }

    return render(request, 'reviews.html', context)


def profile(request):
    """
    Display user profile page.

    Requires user authentication. Redirects to login if user is anonymous.

    Args:
        request (HttpRequest): The HTTP request object

    Returns:
        HttpResponse: Rendered profile.html template or redirect to login

    Note:
        Displays error message and redirects if user not authenticated
    """
    if request.user.is_anonymous:
        messages.error(request, 'Please Login first!!')
        return redirect('login')
    return render(request, 'profile.html')


def manage_menu(request):
    """
    Handle menu item management (adding new dishes).

    GET: Displays the menu management form
    POST: Processes new menu item addition with image upload

    Args:
        request (HttpRequest): The HTTP request object

    Returns:
        HttpResponse: Rendered manage_menu.html template or redirect to menu

    Authorization:
        - Requires authenticated user
        - Requires superuser or cafe_manager permissions

    Form Data (POST):
        name (str): Dish name
        price (decimal): Dish price
        desc (str): Dish description
        cat (str): Dish category
        img (file): Dish image

    Note:
        Automatically assigns list_order based on category for proper sorting
    """
    if request.method == 'POST' and request.FILES['img']:
        # Check user authentication
        if (request.user.is_anonymous):
            messages.error(request, 'Please Login to continue!')
            return redirect('login')
        # Check user permissions (admin or cafe manager)
        if not ((request.user.is_superuser) or (request.user.cafe_manager)):
            messages.error(request, 'Only Staff members are allowed!')
            return redirect('menu')
        else:
            # Extract form data
            name = request.POST.get('name')
            price = request.POST.get('price')
            desc = request.POST.get('desc')
            cat = request.POST.get('cat')
            img = request.FILES['img']

            # Assign list_order based on category for proper menu sorting
            if cat.lower() == 'pizzas':
                listing_order = 1
            elif cat.lower() == 'burgers':
                listing_order = 2
            elif cat.lower() == 'rice':
                listing_order = 3  # Fixed: rice should be 3
            elif cat.lower() == 'kebabs':
                listing_order = 4  # Fixed: kebabs should be 4
            elif cat.lower() == 'wraps':
                listing_order = 5
            elif cat.lower() == 'sides':
                listing_order = 6
            elif cat.lower() == 'drinks':
                listing_order = 7
            elif cat.lower() == 'desserts':
                listing_order = 8

            # Create and save new menu item
            dish = MenuItem(
                name=name,
                price=price,
                desc=desc,
                category=cat.lower(),
                pic=img,
                list_order=listing_order
            )
            dish.save()
            messages.success(request, 'Dish added successfully!')
            return redirect('manage_menu')

    # Get all menu items with images for display
    items = MenuItem.objects.filter(pic__isnull=False).exclude(
        pic='').order_by('list_order')

    return render(
        request,
        'manage_menu.html',
        {'items': items}
    )


def delete_dish(request, item_id):
    """
    Delete a menu item from the database.

    Args:
        request (HttpRequest): The HTTP request object
        item_id (int): ID of the menu item to delete

    Returns:
        HttpResponse: Redirect to menu page

    Authorization:
        Only superusers can delete menu items

    Note:
        Shows error message if non-superuser attempts deletion
    """
    dish = get_object_or_404(MenuItem, id=item_id)
    if request.user.is_superuser:
        if request.method == 'POST':
            dish.delete()
            messages.success(request, 'Item removed successfully')
            return redirect('menu')
    else:
        messages.error(request, 'Only admins are allowed!')
        return redirect('menu')


def cart(request):
    """
    Handle shopping cart display and order processing.

    GET: Displays the cart page
    POST: Processes order submission with cart items

    Args:
        request (HttpRequest): The HTTP request object

    Returns:
        HttpResponse: Rendered cart.html template or redirect based on user status # noqa: E501


    Form Data (POST):
        items_json (str): JSON string of cart items
        table_value (str): Table number or 'null' for takeaway
        price (decimal): Total order price

    Validation:
        - Prevents empty cart submission
        - Validates total price format
        - Handles JSON parsing errors

    Note:
        - Anonymous users receive signup prompt
        - Authenticated users get order count incremented
        - Uses IST timezone adjustment (+5:30 hours)
    """
    from decimal import Decimal, InvalidOperation

    if request.method == 'POST':
        # Determine customer information based on authentication status
        if request.user.is_anonymous:
            name = 'Unknown'
            phone = 'Unknown'
        else:
            name = request.user.first_name + ' ' + request.user.last_name
            phone = request.user.phone

        # Extract order data from form
        items_json = request.POST.get('items_json')
        table_number = request.POST.get('table_value')
        total = request.POST.get('price')

        # Validate cart is not empty
        try:
            cart_dict = json.loads(items_json)
        except (json.JSONDecodeError, TypeError):
            cart_dict = {}

        if not cart_dict or sum(item[0] for item in cart_dict.values()) == 0:
            messages.error(
                request, 'Order unsuccessful: Please add items to cart.')
            return redirect('cart')

        print(f"🧾 Received total from form: {total}")

        # Validate total price
        if not total:
            messages.error(request, 'Order failed: Total price is missing.')
            return redirect('cart')

        try:
            total = Decimal(total)
        except (InvalidOperation, TypeError):
            messages.error(request, 'Order failed: Invalid price format.')
            return redirect('cart')

        # Get current time in IST timezone
        now = datetime.now()
        now_ist = now + timedelta(hours=5, minutes=30)

        # Handle takeaway orders
        if table_number == 'null':
            table_number = 'Take Away'

        # Create and save new order
        new_order = Order(
            name=name,
            phone=phone,
            items_json=items_json,
            table=table_number,
            order_time=now_ist,
            price=total
        )
        new_order.save()

        # Handle post-order actions based on user status
        if request.user.is_anonymous:
            messages.success(
                request,
                'Order Placed thank you! Sign up to save your information'
            )
            return redirect('/')
        else:
            # Increment order count for registered users
            usr = User.objects.get(phone=phone)
            usr.order_count += 1
            usr.save()
            messages.success(request, 'Order Placed! Thank you for ordering')
            return redirect('my_orders')

    return render(request, 'cart.html')


def clear_cart(request):
    """
    Clear all items from the user's cart.

    Args:
        request (HttpRequest): The HTTP request object

    Returns:
        HttpResponse: Rendered cart.html with empty cart or redirect

    Note:
        Only processes POST requests for security
    """
    if request.method == 'POST':
        request.session['cart'] = {}
        total = 0
        messages.success(request, "Cart cleared!")
        context = {
            'cart': {},
            'total': total,
        }
        return render(request, 'cart.html', context)  # ✅ okay here
    return redirect('cart')  # ✅ also okay here


def my_orders(request):
    """
    Display orders for the authenticated user.

    Retrieves and displays all orders associated with the user's phone number,
    grouped by table number.

    Args:
        request (HttpRequest): The HTTP request object

    Returns:
        HttpResponse: Rendered my_orders.html template

    Context:
        order_by_table (dict): User's orders grouped by table

    Note:
        Handles JSON parsing errors in order items gracefully
    """
    phone = request.user.phone

    context = {}
    # Get orders for current user
    orders = Order.objects.filter(phone=phone)
    order_by_table = {}

    # Group orders by table for display
    for key, group in groupby(orders, key=lambda x: x.table):
        order_by_table[key] = list(group)

    # Parse JSON data for each order with error handling
    for table, orders in order_by_table.items():
        for ord in orders:
            items_json_str = ord.items_json
            try:
                ord.items_json = json.loads(items_json_str)
            except (json.JSONDecodeError, TypeError, ValueError):
                ord.items_json = {}  # fallback to empty dict
                print(
                    f"⚠️ JSONDecodeError for order {ord.id}: {items_json_str}")

    context = {'order_by_table': order_by_table}

    return render(request, 'my_orders.html', context)


def login_view(request):
    """
    Handle user authentication.

    GET: Displays login form
    POST: Processes login credentials

    Args:
        request (HttpRequest): The HTTP request object

    Returns:
        HttpResponse: Rendered login.html template or redirect to profile

    Form Data (POST):
        phone (str): User's phone number (username)
        password (str): User's password

    Note:
        Uses phone number as username for authentication
    """
    if request.method == 'POST':
        phone = request.POST.get('phone')
        password = request.POST.get('password')

        user = authenticate(phone=phone, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Logged in successfully !')
            return redirect('profile')

        else:
            messages.error(request, 'Login failed, Invalid Credentials!')
            return redirect('login')

    return render(request, 'login.html')


def Logout(request):
    """
    Log out the current user and redirect to login page.

    Args:
        request (HttpRequest): The HTTP request object

    Returns:
        HttpResponse: Redirect to login page with success message
    """
    logout(request)
    messages.success(request, 'Logged out successfully')
    return redirect('login')


def signup(request):
    """
    Handle user registration.

    GET: Displays registration form
    POST: Processes new user creation

    Args:
        request (HttpRequest): The HTTP request object

    Returns:
        HttpResponse: Rendered signup.html template or redirect to login

    Form Data (POST):
        fname (str): First name
        lname (str): Last name
        number (str): Phone number (used as username)
        password (str): Password
        cpassword (str): Confirm password

    Validation:
        - Checks if phone number already exists
        - Redirects existing users to login

    Note:
        Uses phone number as unique identifier/username
    """
    if request.method == "POST":
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        phone = request.POST.get('number')
        pass_word = request.POST.get('password')
        c_pass_word = request.POST.get('cpassword')

        if User.objects.filter(phone=phone).exists():
            messages.error(
                request,
                'Mobile number already registered. Please log in to continue')
            return redirect('login')

        my_user = User.objects.create_user(phone=phone, password=pass_word)
        my_user.first_name = fname
        my_user.last_name = lname
        my_user.save()
        messages.success(request, 'User created successfully !!')

        return redirect('login')

    return render(request, 'signup.html')


def generate_bill(request):
    """
    Generate and display bill for a specific table.

    Processes all unpaid orders for a table, calculates total,
    marks orders as billed, and creates a bill record.

    Args:
        request (HttpRequest): The HTTP request object

    Query Parameters:
        table (str): Table number to generate bill for

    Returns:
        HttpResponse: Rendered generate_bill.html template with bill details

    Context:
        order_dict (dict): Consolidated order items with quantities and totals
        bill_total (int): Total bill amount
        name (str): Customer name
        phone (str): Customer phone
        inv_id (int): Generated bill/invoice ID

    Note:
        - Consolidates multiple orders into single bill
        - Uses IST timezone (+5:30 hours)
        - Marks orders as bill_clear=True to prevent double billing
    """
    t_number = request.GET.get('table')

    # Get all unbilled orders for the specified table
    order_for_table = Order.objects.filter(table=t_number, bill_clear=False)
    total_bill = 0
    now = datetime.now()
    now_ist = now + timedelta(hours=5, minutes=30)

    bill_items = []
    c_name = ''
    c_phone = ''

    # Process each order and mark as billed
    for o in order_for_table:
        total_bill += int(o.price)
        o.bill_clear = True  # Mark order as billed
        o.save()

        bill_items.append({
            'order_items': o.items_json,
        })
        c_name = o.name
        c_phone = o.phone

    # Consolidate items from multiple orders
    order_dict = {}
    for item in bill_items:
        for key, value in item.items():
            order_items = json.loads(value)
            for pr_key, pr_value in order_items.items():
                # Combine quantities and calculate totals
                order_dict[pr_value[1].lower()] = [
                    pr_value[0], (pr_value[2] * pr_value[0])
                ]

    # Create and save bill record
    new_bill = Bill(order_items=order_dict,
                    name=c_name,
                    bill_total=total_bill,
                    phone=c_phone,
                    bill_time=now_ist)
    new_bill.save()

    context = {}

    context = {
        'order_dict': order_dict,
        'bill_total': total_bill,
        'name': c_name,
        'phone': c_phone,
        'inv_id': new_bill.id,
    }
    return render(request, 'generate_bill.html', context)


def view_bills(request):
    """
    Display all generated bills for admin users.

    Retrieves and displays all bills in the system, ordered by most recent first. # noqa: E501

    Restricted to admin users only.

    Args:
        request (HttpRequest): The HTTP request object

    Returns:
        HttpResponse: Rendered bills.html template or redirect if unauthorized

    Context:
        bills (QuerySet): All bills ordered by bill_time descending

    Authorization:
        Only authenticated admin users can access this view

    Note:
        Converts order_items string representation back to dict for display
    """
    # Check if user is authenticated (admin check)
    if request.user.is_anonymous:
        messages.error(request, 'You Must be an admin user to view this!')
        return redirect('')

    # Get all bills ordered by newest first
    all_bills = Bill.objects.all().order_by('-bill_time')

    # Convert string representation back to dict for template display
    for b in all_bills:
        b.order_items = ast.literal_eval(b.order_items)

    context = {'bills': all_bills}

    return render(request, 'bills.html', context)


def edit_profile(request):
    """
    Handle user profile editing.

    GET: Displays profile editing form
    POST: Processes profile updates including name, phone, and password changes

    Args:
        request (HttpRequest): The HTTP request object

    Returns:
        HttpResponse: Rendered edit_profile.html template or redirect to profile  # noqa: E501

    Authorization:
        Requires authenticated user

    Form Data (POST):
        first_name (str): User's first name
        last_name (str): User's last name
        phone (str): User's phone number
        current_password (str): Current password (required for password change)
        new_password (str): New password (optional)
        confirm_password (str): Confirmation of new password (optional)

    Validation:
        - Checks if phone number is already taken by another user
        - Validates current password before allowing password change
        - Ensures new password and confirmation match

    Note:
        Phone number serves as username, so changes affect login credentials
    """
    if request.user.is_anonymous:
        messages.error(request, 'Please login first!')
        return redirect('login')

    if request.method == 'POST':
        # Get form data
        first_name = request.POST.get('first_name', '').strip()
        last_name = request.POST.get('last_name', '').strip()
        phone = request.POST.get('phone', '').strip()
        current_password = request.POST.get('current_password', '')
        new_password = request.POST.get('new_password', '')
        confirm_password = request.POST.get('confirm_password', '')

        # Validate required fields
        if not first_name or not last_name or not phone:
            messages.error(request, 'All fields are required!')
            return render(request, 'edit_profile.html')

        # Check if phone number is already taken by another user
        if phone != request.user.phone:
            if User.objects.filter(phone=phone).exists():
                messages.error(
                    request, 'This phone number is already registered!')
                return render(request, 'edit_profile.html')

        # Handle password change if requested
        if new_password or confirm_password:
            if not current_password:
                messages.error(
                    request, 'Current password is required to change password!')  # noqa: E501
                return render(request, 'edit_profile.html')

            if not request.user.check_password(current_password):
                messages.error(request, 'Current password is incorrect!')
                return render(request, 'edit_profile.html')

            if new_password != confirm_password:
                messages.error(request, 'New passwords do not match!')
                return render(request, 'edit_profile.html')

            if len(new_password) < 8:
                messages.error(
                    request, 'New password must be at least 8 characters long!')  # noqa: E501
                return render(request, 'edit_profile.html')

        # Update user information
        user = request.user
        user.first_name = first_name
        user.last_name = last_name
        user.phone = phone

        # Update password if provided
        if new_password:
            user.set_password(new_password)

        user.save()

        # If password was changed, re-authenticate the user
        if new_password:
            from django.contrib.auth import login
            login(request, user)
            messages.success(
                request, 'Profile and password updated successfully!')
        else:
            messages.success(request, 'Profile updated successfully!')

        return redirect('profile')

    return render(request, 'edit_profile.html')


def create_review(request):
    """Create a new review using ReviewForm."""
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.r_date = datetime.now()
            review.save()
            messages.success(
                request, 'Your review has been submitted successfully!')
            return redirect('home')  # Redirect to home or reviews page
        else:
            messages.error(
                request, 'Please correct the errors in your review.')
    else:
        form = ReviewForm()

    # Return form as JSON for AJAX or simple HTML response
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return JsonResponse({
            'form_html': form.as_p(),
            'success': form.is_valid() if request.method == 'POST' else None
        })

    return HttpResponse(f"""
    <form method="post">
        <input type="hidden" name="csrfmiddlewaretoken" value="{request.META.get('CSRF_COOKIE')}">  # noqa: E501
        {form.as_p()}
        <button type="submit">Submit Review</button>
    </form>
    """)


@login_required
def edit_review(request, review_id):
    """Edit an existing review using ReviewForm - only allow editing own reviews."""  # noqa: E501
    review = get_object_or_404(Rating, id=review_id)

    # Check if the review belongs to the current user
    current_user_name = f"{request.user.first_name} {request.user.last_name}"
    if review.name != current_user_name:
        messages.error(request, 'You can only edit your own reviews!')
        return redirect('reviews')

    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            # Use Django's built-in has_changed method to detect changes
            if not form.has_changed():
                messages.info(request, 'No changes were made to your review.')
                # Don't redirect, stay on the edit page to show the message
                context = {
                    'form': form,
                    'review': review,
                    'is_editing': True
                }
                return render(request, 'edit_review.html', context)
            else:
                # Save the changes and update the timestamp
                updated_review = form.save(commit=False)
                updated_review.r_date = datetime.now()  # Update timestamp to current time  # noqa: E501
                updated_review.save()
                messages.success(request, 'Review successfully updated!')
                return redirect('reviews')
        else:
            messages.error(
                request, 'Please correct the errors in your review.')
    else:
        form = ReviewForm(instance=review)

    context = {
        'form': form,
        'review': review,
        'is_editing': True
    }
    return render(request, 'edit_review.html', context)


@login_required
def delete_review(request, review_id):
    """Delete a review with confirmation - only allow deleting own reviews."""
    review = get_object_or_404(Rating, id=review_id)

    # Check if the review belongs to the current user
    current_user_name = f"{request.user.first_name} {request.user.last_name}"
    if review.name != current_user_name:
        messages.error(request, 'You can only delete your own reviews!')
        return redirect('reviews')

    if request.method == 'POST':
        form = DeleteConfirmForm(request.POST)
        if form.is_valid() and form.cleaned_data['confirm']:
            review_name = review.name
            review.delete()
            messages.success(
                request, 'Your review has been deleted successfully!')
            return redirect('reviews')
    else:
        form = DeleteConfirmForm()

    context = {
        'form': form,
        'review': review,
        'is_deleting': True
    }
    return render(request, 'delete_review.html', context)


def list_reviews(request):
    """List all reviews with edit/delete links for authenticated users."""
    reviews = Rating.objects.all().order_by('-r_date')

    # Display messages if any
    messages_html = ""
    if hasattr(request, '_messages'):
        for message in messages.get_messages(request):
            messages_html += f'<div class="alert alert-{message.tags}">{message}</div>'  # noqa: E501

    reviews_html = ""
    for review in reviews:
        # Show edit/delete buttons only for authenticated users
        buttons_html = ""
        if request.user.is_authenticated:
            buttons_html = f"""
            <div style="margin-top: 10px;">
                <a href="/reviews/edit/{review.id}/" style="background-color: #007bff; color: white; padding: 5px  # noqa: E501
                10px; text-decoration: none; border-radius: 3px; margin-right: 5px;">Edit</a>
                <a href="/reviews/delete/{review.id}/" style="background-color: #dc3545; color: white; padding: 5px 10px; text-decoration: none; border-radius: 3px;">Delete</a>
            </div>
            """

        reviews_html += f"""
        <div style="border: 1px solid #ddd; padding: 15px; margin: 10px 0; border-radius: 5px; background-color: #f9f9f9;">  # noqa: E501
            <h4 style="color: #333; margin: 0 0 10px 0;">{review.name}</h4>
            <p style="margin: 0 0 10px 0; line-height: 1.5;">{review.comment}</p>
            <small style="color: #666;">📅 {review.r_date.strftime('%B %d, %Y at %I:%M %p')}</small>
            {buttons_html}
        </div>
        """

    auth_status = f"<p>Authentication Status: {'Logged in' if request.user.is_authenticated else 'Not logged in'}</p>"  # noqa: E501
