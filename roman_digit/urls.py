from django.urls import path
from roman_digit import views

urlpatterns = [
    path('', views.index, name='index'),
]