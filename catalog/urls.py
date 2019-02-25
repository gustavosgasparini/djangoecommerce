from django.urls import path
from . import views

app_name = 'catalog'

urlpatterns = [
    path('produtos/', views.product_list, name='product_list'),
    path('produtos/<str:slug>/', views.categories, name='category'),
]