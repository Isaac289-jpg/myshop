from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('orders/', views.orders_list, name='orders'),
]
from django.urls import path
from . import views

urlpatterns = [
    path("order/", views.create_order, name="create_order"),
]
from django.urls import path
from . import views

urlpatterns = [
    path("products/", views.products_list, name="products"),
    path("cart/add/", views.add_to_cart, name="add_to_cart"),
    path("order/", views.create_order, name="create_order"),
    path("orders/", views.orders_list, name="orders"),
]
from django.urls import path
from . import views

urlpatterns = [
    path("health/", views.health_check, name="health"),
]
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("shop.urls")),  # include shop app URLs
]
from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.products, name='products'),
    path('cart/add/', views.add_to_cart, name='add_to_cart'),
    path('order/', views.create_order, name='create_order'),
    path('orders/', views.orders, name='orders'),
    path('health/', views.health_check, name='health_check'),  # ✅ Add this
]
