from django import forms
from django.conf import settings
from django.core.mail import send_mail


class ContactForm(forms.Form):

    name = forms.CharField(label='Nome')
    email = forms.EmailField(label='E-Mail')
    message = forms.CharField(label='Mensagem', widget=forms.Textarea())

    def send_email(self):
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        message = self.cleaned_data['message']
        message = f'Nome: {name}\nE-Mail: {email}\n{message}'
        send_mail(
            'Contato do Django E-Commerce', message, settings.DEFAULT_FROM_EMAIL, 
            [settings.DEFAULT_FROM_EMAIL]
        )