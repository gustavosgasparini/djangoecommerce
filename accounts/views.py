from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy

from accounts.models import User
from .forms import UserAdminCreationForm


# Create your views here.
class RegisterView(CreateView):

    model = User
    form_class = UserAdminCreationForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('index')