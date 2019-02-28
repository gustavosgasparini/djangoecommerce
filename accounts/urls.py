from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('registro/', views.RegisterView.as_view(), name='register'),
]