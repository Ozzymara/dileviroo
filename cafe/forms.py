"""
Forms for Cafe Application.

This module defines Django forms for handling user input and validation,
specifically for review management including create, edit, and delete operations.  # noqa: E501
"""

from django import forms
from .models import Rating


class ReviewForm(forms.ModelForm):
    """
    Form for creating and editing customer reviews.

    This form provides interface for customers to submit and modify reviews
    with proper validation.
    """

    class Meta:
        model = Rating
        fields = ['comment']  # Remove 'name' field - only allow editing comment  # noqa: E501
        widgets = {
            'comment': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Write your review here...',
                'rows': 4,
                'maxlength': '250'
            }),
        }
        labels = {
            'comment': 'Review Comment',
        }


class DeleteConfirmForm(forms.Form):
    """
    Simple confirmation form for delete operations.
    """
    confirm = forms.BooleanField(
        required=True,
        widget=forms.HiddenInput(),
        initial=True
    )
