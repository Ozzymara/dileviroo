"""
URL Configuration for Cafe Application.

This module defines the URL routing patterns for the cafe Django application,
mapping URL paths to their corresponding view functions. It handles all the
web endpoints for restaurant functionality including menu display, order
management, user authentication, and administrative features.

URL Patterns:
    Public URLs:
        - '' (root): Menu display page
        - 'offers': Special offers and promotions
        - 'reviews': Customer reviews display and submission
        - 'cart': Shopping cart management

    Authentication URLs:
        - 'login': User login page
        - 'signup': User registration page
        - 'logout': User logout functionality

    User-Specific URLs:
        - 'profile': User profile page (authenticated users)
        - 'my_orders': User's order history (authenticated users)

    Administrative URLs:
        - 'all_orders': View all orders (staff only)
        - 'manage_menu': Add/edit menu items (staff only)
        - 'delete_dish/<int:item_id>/': Delete menu items (admin only)
        - 'generate_bill': Generate bills for tables (staff only)
        - 'view_bills': View all generated bills (admin only)

    Media URLs:
        - Static media files served in DEBUG mode for development

Note:
    - URLs are designed for a restaurant management system
    - Some URLs require authentication or specific permissions
    - Media files are served in development mode only
    - Commented checkout path suggests future payment integration
"""

from django.contrib import admin
from django.urls import path, include
from cafe import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Main application URLs
    # path('', views.home, name='home'),  # Commented home page
    path('', views.menu, name='menu'),  # Root URL displays menu

    # Menu management URLs (admin/staff only)
    path('delete_dish/<int:item_id>/', views.delete_dish,
         name='delete_dish'),  # Delete menu item
    path('manage_menu', views.manage_menu,
         name='manage_menu'),  # Add new menu items

    # Public content URLs
    path('offers', views.offers, name='offers'),  # Special offers page
    path('reviews', views.reviews, name='reviews'),  # Customer reviews

    # Review CRUD operations
    path('reviews/', views.list_reviews, name='list_reviews'),
    path('reviews/create/', views.create_review, name='create_review'),
    path('reviews/edit/<int:review_id>/', views.edit_review, name='edit_review'),
    path('reviews/delete/<int:review_id>/', views.delete_review, name='delete_review'),

    # User account URLs
    # User profile (auth required)
    path('profile', views.profile, name='profile'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('login', views.login_view, name='login'),  # User login
    path('signup', views.signup, name='signup'),  # User registration
    path('logout', views.Logout, name='logout'),  # User logout

    # Order management URLs
    path('cart', views.cart, name='cart'),  # Shopping cart
    # path('checkout', views.checkout, name='checkout'),
    # Future payment integration
    path('my_orders', views.my_orders, name='my_orders'),  # User order history
    # All orders (staff only)
    path('all_orders', views.all_orders, name='all_orders'),

    # Billing URLs (staff/admin only)
    path('generate_bill', views.generate_bill,
         name='generate_bill'),  # Generate table bills
    path('view_bills', views.view_bills, name='view_bills'),  # View all bills
]

# Serve media files in development mode
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
