"""
Django Application Configuration for Cafe Application.

This module defines the configuration for the cafe Django application,
which handles restaurant management functionality including menu management,
order processing, user authentication, and billing systems.

The cafe application provides:
- Menu item management and display
- Customer order processing and tracking
- User authentication with phone-based login
- Review and rating system
- Bill generation and management
- Admin interface for restaurant staff
"""

from django.apps import AppConfig


class CafeConfig(AppConfig):
    """
    Configuration class for the Cafe Django application.

    This class defines the basic configuration settings for the cafe app,
    including the default auto field type and the application name.

    Attributes:
        default_auto_field (str): Specifies the default primary key field type
                                 for models that don't explicitly define one
        name (str): The name of the Django application

    Note:
        This configuration is automatically loaded when the app is included
        in Django's INSTALLED_APPS setting.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cafe'
