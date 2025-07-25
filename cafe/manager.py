"""
Custom User Manager for Phone-Based Authentication.

This module defines a custom user manager that handles user creation
and authentication using phone numbers instead of the default username/email
system. It extends Django's BaseUserManager to provide phone-based
user management functionality for the cafe application.

Classes:
    UserManager: Custom manager for creating users with phone authentication
"""

from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    """
    Custom user manager for phone number-based authentication.
    
    This manager handles the creation of regular users and superusers
    using phone numbers as the unique identifier instead of usernames.
    It extends Django's BaseUserManager to provide custom user creation
    logic suitable for the cafe application's authentication system.
    
    Attributes:
        use_in_migrations (bool): Enables this manager to be used during migrations
    
    Methods:
        create_user: Creates a regular user with phone number authentication
        create_superuser: Creates a superuser with administrative privileges
    """
    use_in_migrations = True

    def create_user(self, phone, password=None, **extra_fields):
        """
        Create and return a regular user with phone number authentication.
        
        Creates a new user instance using the provided phone number as the
        unique identifier. Sets the password and saves the user to the database.
        
        Args:
            phone (str): The user's phone number (required, used as username)
            password (str, optional): The user's password. Defaults to None.
            **extra_fields: Additional fields to set on the user model
            
        Returns:
            User: The created user instance
            
        Raises:
            ValueError: If phone number is not provided
            
        Note:
            Phone number is required as it serves as the unique identifier
            for authentication in place of traditional username/email
        """
        # Validate that phone number is provided
        if not phone:
            raise ValueError('Phone is required')

        # Create user instance with phone and any additional fields
        user = self.model(phone=phone, **extra_fields)
        # Set and hash the password
        user.set_password(password)
        # Save user to database
        user.save(using=self._db)

        return user

    def create_superuser(self, phone, password, **extra_fields):
        """
        Create and return a superuser with administrative privileges.
        
        Creates a superuser with all necessary permissions for accessing
        the Django admin interface and managing the cafe application.
        Sets default values for staff, active, and superuser status.
        
        Args:
            phone (str): The superuser's phone number (required)
            password (str): The superuser's password (required)
            **extra_fields: Additional fields to set on the user model
            
        Returns:
            User: The created superuser instance
            
        Note:
            Automatically sets is_staff=True, is_active=True, and is_superuser=True
            These permissions are required for admin access and management functions
        """
        # Set default superuser permissions
        extra_fields.setdefault('is_staff', True)      # Can access admin interface
        extra_fields.setdefault('is_active', True)     # Account is active
        extra_fields.setdefault('is_superuser', True)  # Has all permissions

        # Create superuser using the regular create_user method
        return self.create_user(phone, password, **extra_fields)
