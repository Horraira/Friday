from django.urls import path
from . import views

urlpatterns = [
    path('dropdown/', views.dropdown, name='dropdown'),
]
