from django import forms
from django.contrib.auth.forms import (AuthenticationForm, PasswordResetForm,
                                       SetPasswordForm)

from .models import UserBase


class RegistrationForm(forms.ModelForm):
    """
    Form for registering a new user account.    
    """
    user_name = forms.CharField(label='Enter Username', max_length=50, required=True, help_text='Required')
    email = forms.EmailField(label='Enter Email', max_length=100, required=True, help_text='Required',
                             error_messages={"required": "Sorry, you will need an email"})
    password = forms.CharField(label='Enter Password', max_length=100, required=True, widget=forms.PasswordInput)
    confirm_password = forms.CharField(label='Confirm Password', max_length=100,
                                       required=True, widget=forms.PasswordInput)

    class Meta:
        model = UserBase
        fields = ('user_name', 'email',)
    
