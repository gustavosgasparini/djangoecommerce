from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View, TemplateView, CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy

from core.forms import ContactForm

User = get_user_model()


# Create your views here.
class IndexView(TemplateView):

    template_name = 'index.html'


def contact(request):
    success = False
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.send_email()
        success = True
   
    context = {
        'form': form,
        'success': success,
    }

    return render(request, 'contact.html', context)


class RegisterView(CreateView):

    form_class = UserCreationForm
    template_name = 'register.html'
    model = User
    success_url = reverse_lazy('index')