from django.urls import path

from . import views

urlpatters = [
    path('', views.basket_summary, name='basket_summary'),
]
