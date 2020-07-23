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
    path('product-list/', views.productList, name="task-list")
    

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)