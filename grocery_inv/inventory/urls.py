"""Defines URL patterns for inventory."""
from django.urls import path
from . import views

app_name = 'inventory'
urlpatterns = [
    # Home Page
    path('', views.index, name='index'),
    path('inventory/', views.inventory, name='inventory'),
    path('add_item/', views.add_item, name='add_item'),
    path('edit_item/<int:pk>/', views.edit_item, name='edit_item'),
    path('delete_item/<int:pk>/', views.delete_item, name='delete_item'),

]