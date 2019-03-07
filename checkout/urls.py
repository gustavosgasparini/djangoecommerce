from django.urls import path
from checkout import views

app_name = 'checkout'

urlpatterns = [
    path('carrinho/adicionar/<str:slug>', views.CreateCartItemView.as_view(), name='create_cartitem'),
]