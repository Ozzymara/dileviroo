"""
Forms for Cafe Application.

This module defines Django forms for handling user input and validation,
specifically for review management including create, edit, and delete operations.
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
        fields = ['name', 'comment']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your name',
                'maxlength': '30'
            }),
            'comment': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Write your review here...',
                'rows': 4,
                'maxlength': '250'
            }),
        }
        labels = {
            'name': 'Your Name',
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
