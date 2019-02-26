from django.shortcuts import render
from django.http import HttpResponse

from core.forms import ContactForm

# Create your views here.
def index(request):
    return render(request, 'index.html')


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