"""
Main URL Configuration for Dileviroo Restaurant Management System.

This is the root URL configuration for the Dileviroo project, a comprehensive
restaurant management system built with Django. It routes URLs to the appropriate
applications and provides development tools integration.

Project Structure:
    - Main application: 'cafe' - handles all restaurant functionality
    - Admin interface: Django's built-in admin for data management
    - Debug toolbar: Development debugging tools (DEBUG mode only)

URL Patterns:
    - '__debug__/': Django Debug Toolbar URLs (development only)
    - 'admin': Django admin interface for data management
    - '': Root URL includes cafe application URLs

Applications Included:
    - cafe: Restaurant management (menu, orders, billing, users)
    - admin: Django administrative interface
    - debug_toolbar: Development debugging tools

The cafe application handles:
    - Menu item management and display
    - Customer order processing and tracking
    - User authentication with phone-based login
    - Customer review and rating system
    - Bill generation and management
    - Administrative functions for restaurant staff

Note:
    Debug toolbar is included for development debugging and should be
    disabled in production environments.
"""

import debug_toolbar

from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    # Development debugging tools (DEBUG mode only)
    path('__debug__/', include(debug_toolbar.urls)),
    
    # Django admin interface for data management
    path('admin', admin.site.urls),  # ✅ This line is essential
    
    # Include all cafe application URLs at root level
    path('', include('cafe.urls')),
]
