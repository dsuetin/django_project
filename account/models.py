"""Account model"""
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,
                                        PermissionsMixin)
from django.core.mail import send_mail
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField


class CustomAccountManager(BaseUserManager):
    """
    Class for account managment
    """
    def create_superuser(self, email, user_name, password, **other_fields):
        """Create new superuser"""
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email=email, user_name=user_name, password=password, **other_fields)

    def create_user(self, email, user_name, password, **other_fields):
        """Create new user"""
        if not email:
            raise ValueError(_('Users must have an email address'))

        # other_fields.setdefault('is_staff', False)
        # other_fields.setdefault('is_superuser', False)
        # other_fields.setdefault('is_active', True)

        email = self.normalize_email(email)
        user = self.model(email=email, user_name=user_name, **other_fields)
        user.set_password(password)
        user.save()
        return user


class UserBase(AbstractBaseUser, PermissionsMixin):
    """_summary_

    Args:
        AbstractBaseUser (_type_): _description_
        PermissionsMixin (_type_): _description_

    Returns:
        _type_: _description_
    """
    email = models.EmailField(_('email address'), unique=True)
    user_name = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=150, blank=True)
    about = models.TextField(_
                             ('about'), max_length=500, blank=True)
    # Delivery details
    country = CountryField()
    town_city = models.CharField(max_length=150, blank=True)
    address_line_1 = models.CharField(max_length=150, blank=True)
    address_line_2 = models.CharField(max_length=150, blank=True)
    postcode = models.CharField(max_length=150, blank=True)

    # User Status
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name']

    class Meta:
        verbose_name = "Accounts"
        verbose_name_plural = "Accounts"

    def email_user(self, subject, message):
        """ function send email to user """
        send_mail(
            subject,
            message,
            "1@1.com",
            [self.email],
            fail_silently=False,
        )

    def __str__(self) -> str:
        return str(self.user_name)
