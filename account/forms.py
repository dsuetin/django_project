# from collections.abc import Mapping
# from typing import Any
from django import forms
# from django.contrib.auth.forms import (AuthenticationForm, PasswordResetForm,
#                                        SetPasswordForm)
# from django.core.files.base import File
# from django.db.models.base import Model
# from django.forms.utils import ErrorList

from .models import UserBase


class RegistrationForm(forms.ModelForm):
    """
    Form for registering a new user account.    
    """
    user_name = forms.CharField(label='Username', max_length=50, required=True, help_text='Required')
    email = forms.EmailField(label='Email', max_length=100, required=True, help_text='Required',
                             error_messages={"required": "Sorry, you will need an email"})
    password = forms.CharField(label='Password', max_length=100, required=True, widget=forms.PasswordInput)
    confirm_password = forms.CharField(label='Confirm Password', max_length=100,
                                       required=True, widget=forms.PasswordInput)

    class Meta:
        model = UserBase
        fields = ('user_name', 'email',)

    def clean_username(self):
        user_name = self.cleaned_data["user_name"].lower()
        r = UserBase.objects.filter(user_name=user_name)
        if r.count():
            raise forms.ValidationError("Sorry, that username is already taken")
        return user_name

    def clean_confirm_password(self):
        cleaned_data = self.cleaned_data
        if cleaned_data.get("confirm_password") != cleaned_data.get("password"):
            raise forms.ValidationError("Passwords do not match")
        return cleaned_data["confirm_password"]

    def clean_email(self):
        email = self.cleaned_data["email"].lower()
        if UserBase.objects.filter(email=email).exists():
            raise forms.ValidationError("Sorry, that email is already taken")
        return email

    def __init__(self, *args, **kwards) -> None:
        super().__init__(*args, **kwards)
        self.fields["user_name"].widget.attrs.update({"class": "form-control mb-3", "placeholder": "Enter username"})
        self.fields["email"].widget.attrs.update({"class": "form-control mb-3",
                                                  "placeholder": "Enter email",
                                                  'name': 'email',
                                                  'id': 'id_email'})
        self.fields["password"].widget.attrs.update({"class": "form-control mb-3", "placeholder": "Enter password"})
        self.fields["confirm_password"].widget.attrs.update({"class": "form-control mb-3",
                                                             "placeholder": "Confirm password"})

