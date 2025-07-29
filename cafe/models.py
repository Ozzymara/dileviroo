"""
Django Models for Cafe Application.

This module defines the database models for the cafe management system,
including user authentication, menu management, order processing, and billing.
The models support phone-based authentication and comprehensive restaurant
operations management.

Models:
    User: Custom user model with phone-based authentication
    MenuItem: Restaurant menu items with categories and pricing
    Rating: Customer reviews and ratings
    Order: Customer orders with detailed information
    Bill: Generated bills for completed orders

Manager:
    UserManager: Custom manager for phone number-based user creation
"""

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    """
    Custom user manager for phone number-based authentication.

    Handles creation of users and superusers using phone numbers
    as the unique identifier instead of usernames or emails.

    Methods:
        create_user: Creates regular users with phone authentication
        create_superuser: Creates admin users with elevated privileges
    """

    def create_user(self, phone, password=None, **extra_fields):
        """
        Create and return a regular user with phone authentication.

        Args:
            phone (str): User's phone number (required, unique identifier)
            password (str, optional): User's password
            **extra_fields: Additional user model fields

        Returns:
            User: Created user instance

        Raises:
            ValueError: If phone number is not provided
        """
        if not phone:
            raise ValueError('Phone number is required')
        extra_fields.setdefault('is_active', True)
        user = self.model(phone=phone, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone, password=None, **extra_fields):
        """
        Create and return a superuser with administrative privileges.

        Args:
            phone (str): Superuser's phone number
            password (str, optional): Superuser's password
            **extra_fields: Additional user model fields

        Returns:
            User: Created superuser instance with admin privileges
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(phone, password, **extra_fields)


class User(AbstractUser):
    """
    Custom user model with phone-based authentication.

    Extends Django's AbstractUser to use phone numbers instead of
    usernames for authentication. Includes additional fields for
    cafe-specific functionality like order tracking and manager status.

    Attributes:
        phone (CharField): Unique phone number
        (max 10 digits, primary identifier)
        phone_verified (BooleanField): Whether phone number is verified
        cafe_manager (BooleanField): Whether user has cafe manager privileges
        order_count (IntegerField): Total number of orders placed by user

    Meta:
        USERNAME_FIELD: Uses 'phone' instead of 'username'
        REQUIRED_FIELDS: Empty list (only phone required)

    Note:
        - email and username fields are disabled (set to None)
        - Phone number serves as the unique identifier for authentication
        - Compatible with Django's authentication system
    """
    email = None
    username = None
    phone = models.CharField(max_length=10, unique=True)
    phone_verified = models.BooleanField(default=False)
    cafe_manager = models.BooleanField(default=False)
    order_count = models.IntegerField(default=0)

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []
    objects = UserManager()

    def __str__(self):
        """Return string representation of user (phone number)."""
        return self.phone


class MenuItem(models.Model):
    """
    Model representing a restaurant menu item.

    Stores information about dishes including name, category, description,
    image, price, and display order for menu organization.

    Attributes:
        name (CharField): Item name (max 50 characters)
        category (CharField): Item category (max 50 characters)
        desc (CharField): Item description (max 250 characters)
        pic (ImageField): Item image uploaded to 'fimage' directory
        price (CharField): Item price as string (max 4 characters)
        list_order (IntegerField): Display order within category

    Note:
        - Price stored as string for flexibility in display formatting
        - list_order determines the sequence items appear in menus
        - Images are stored in the 'fimage' upload directory
    """
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default='')
    desc = models.CharField(max_length=250)
    pic = models.ImageField(upload_to='fimage')
    price = models.CharField(max_length=4, default='0')
    list_order = models.IntegerField(default=0)

    def __str__(self):
        """Return string representation of menu item (name)."""
        return self.name


class Rating(models.Model):
    """
    Model representing customer reviews and ratings.

    Stores customer feedback including reviewer name, comment text,
    and the date and time the review was submitted.

    Attributes:
        name (CharField): Reviewer's name (max 30 characters)
        comment (CharField): Review comment text (max 250 characters)
        r_date (DateTimeField): Date and time when review was submitted

    Note:
        - Reviews are associated with customer names, not user accounts
        - Used for displaying customer feedback on the website
        - DateTime field helps with chronological ordering of reviews
    """
    name = models.CharField(max_length=30)
    comment = models.CharField(max_length=250)
    r_date = models.DateTimeField()

    def __str__(self):
        """Return string representation of rating
        (reviewer's name + 'review')."""
        return f"{self.name}\'s review"


class Order(models.Model):
    """
    Model representing a customer order.

    Stores comprehensive order information including items ordered (as JSON),
    customer details, table assignment, pricing, timing, and billing status.

    Attributes:
        order_id (IntegerField): Order identifier (default 0)
        items_json (CharField): JSON string of ordered items (max 5000 chars)
        name (CharField): Customer name (max 30 characters)
        phone (CharField): Customer phone number (max 10 digits)
        table (CharField): Table number or 'take away' (max 15 characters)
        price (CharField): Total order price as string (max 5 characters)
        order_time (DateTimeField): Timestamp when order was placed
        bill_clear (BooleanField):
        Whether order has been billed (default False)

    Note:
        - items_json stores order details in JSON format for flexibility
        - bill_clear prevents double billing of orders
        - Supports both dine-in (table number) and takeaway orders
        - Phone links orders to registered users when applicable
    """
    order_id = models.IntegerField(default=0)
    items_json = models.CharField(max_length=5000)
    name = models.CharField(max_length=30, default='')
    phone = models.CharField(max_length=10, default='')
    table = models.CharField(max_length=15, default='take away')
    price = models.CharField(max_length=5, default='0')
    order_time = models.DateTimeField()
    bill_clear = models.BooleanField(default=False)


class Bill(models.Model):
    """
    Model representing a generated bill for completed orders.

    Consolidates multiple orders into a single bill for payment processing.
    Stores itemized order details, customer information, and billing timestamp.

    Attributes:
        order_items (CharField):
        Consolidated order items as string (max 5000 chars)
        name (CharField): Customer name (max 50 characters)
        bill_total (IntegerField): Total bill amount
        phone (CharField): Customer phone number (max 10 digits)
        bill_time (DateTimeField): Timestamp when bill was generated

    Note:
        - Consolidates multiple orders from the same table/customer
        - order_items contains processed order data for billing
        - Used for final payment processing and record keeping
        - Links to customer via phone number for order history
    """
    order_items = models.CharField(max_length=5000)
    name = models.CharField(default='', max_length=50)
    bill_total = models.IntegerField()
    phone = models.CharField(max_length=10)
    bill_time = models.DateTimeField()