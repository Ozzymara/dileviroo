from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from functools import wraps


def admin_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        # Check if user is authenticated first
        if not request.user.is_authenticated:
            messages.error(request, 'Please login to access this page.')
            return redirect('login')

        # Then check if user is admin
        if not request.user.is_staff and not request.user.is_superuser:
            messages.error(request, 'Admin access required to view this page.')
            return redirect('login')

        return view_func(request, *args, **kwargs)
    return _wrapped_view
