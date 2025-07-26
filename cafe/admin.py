"""
Django Admin Configuration for Cafe Application.

This module configures the Django admin interface for managing cafe-related models including menu items, user accounts, orders, ratings, and bills. It provides customized admin interfaces with enhanced functionality for restaurant management. # noqa: E501

Models Registered:
    - MenuItem: Restaurant menu items with custom display and filtering
    - User: Custom user model with phone-based authentication
    - Rating: Customer reviews and ratings
    - Order: Customer orders with detailed information
    - Bill: Generated bills for completed orders
"""

from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .models import MenuItem, Rating, Order, Bill


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    """
    Admin interface configuration for MenuItem model.

    Provides enhanced admin interface for managing restaurant menu items
    with display optimization, search functionality, and filtering options.

    Features:
        - List display shows key item information (name, price, category)
        - Search functionality by item name
        - Filter options by category for easy navigation
        - Automatic registration with MenuItem model

    Attributes:
        list_display (list): Fields to display in the admin list view
        search_fields (list): Fields to enable search functionality
        list_filter (list): Fields to provide filtering options
    """
    list_display = ['name', 'price', 'category', 'list_order']
    search_fields = ['name', 'price', 'category', 'list_order']
    list_filter = ['price', 'category']


# Get the custom user model for registration
User = get_user_model()


class CustomUserAdmin(UserAdmin):
    """
    Customized admin interface for User model.

    Extends Django's built-in UserAdmin to accommodate the custom user model
    that uses phone numbers instead of usernames for authentication.

    Features:
        - Orders users by phone number for logical sorting
        - Inherits all standard UserAdmin functionality
        - Compatible with phone-based authentication system

    Attributes:
        ordering (list): Default ordering for user list (by phone number)

    Note:
        Uses phone number as the primary identifier instead of username
    """
    ordering = ['phone']


# Register the custom user model with the customized admin
admin.site.register(User, CustomUserAdmin)

# Register remaining models with default admin interface
"""
Additional Model Registrations:

Rating: Customer reviews and ratings management
- Allows admin to view and moderate customer feedback
- Default admin interface provides basic CRUD operations

Order: Customer order management
- Enables admin to view all customer orders
- Useful for order tracking and customer service
- Default interface shows all order fields

Bill: Generated bill management
- Provides access to all generated bills
- Useful for accounting and financial tracking
- Default interface displays bill details and totals
"""
admin.site.register(Rating)
admin.site.register(Order)
admin.site.register(Bill)
