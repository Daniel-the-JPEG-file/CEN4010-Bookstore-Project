from django.urls import path
from . import views

urlpatterns = [
    path('cart/<int:user_id>/', views.get_cart, name='get_cart'),
    path('cart/<int:user_id>/subtotal/', views.get_subtotal, name='get_subtotal'),
    path('cart/add/', views.add_to_cart, name='add_to_cart'),
    path('cart/remove/', views.remove_from_cart, name='remove_from_cart'),
]