from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.welcome, name="welcome"),
    path('store/', views.store, name="store"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('update_item/', views.updateItem, name="update_item"),
    path('api/', views.apiOverview, name="api-overview"),
    path('product-list/', views.productList, name="product-list"),
    path('product/<str:pk>/', views.product, name="product"),
    path('order-list/', views.orderList, name="order-list"),
    path('orderItem-list/', views.orderItemList, name="orderItem-list"),
    path('process_order/', views.processOrder, name="process_order")

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)