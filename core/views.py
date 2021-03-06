from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View, TemplateView
from django.contrib import messages

from core.forms import ContactForm



# Create your views here.
class IndexView(TemplateView):

    template_name = 'index.html'


def contact(request):
    success = False
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.send_email()
        success = True
    elif request.method == 'POST':
        messages.error(request, 'Formulário inválido. Preencha todos os campos corretamente.')
   
    context = {
        'form': form,
        'success': success,
    }

    return render(request, 'contact.html', context)
    