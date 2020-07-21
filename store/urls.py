from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name="welcome"),
    path('store/', views.store, name="store"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
]