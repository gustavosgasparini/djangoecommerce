from django.urls import path
from . import views

app_name = 'catalog'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('<str:slug>/', views.categories, name='category'),
    path('produto/<str:slug>', views.products, name='product'),
]