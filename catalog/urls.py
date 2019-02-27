from django.urls import path
from . import views

app_name = 'catalog'

urlpatterns = [
    path('', views.ProductListView.as_view(), name='product_list'),
    path('<str:slug>/', views.CategoryListView.as_view(), name='category'),
    path('produto/<str:slug>', views.ProductsView.as_view(), name='product'),
]