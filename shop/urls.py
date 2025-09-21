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
