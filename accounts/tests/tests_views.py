from django.test import TestCase, Client
from django.urls import reverse
from accounts.models import User
from django.conf import settings

from model_mommy import mommy
# Create your tests here.
class RegisterViewTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.register_url = reverse('accounts:register')

    def test_register_ok(self):
        data = {'username':'admin', 'email': 'admin@admin.com', 'password1': 'fulano159', 'password2': 'fulano159'}
        response = self.client.post(self.register_url, data)
        redirect_url = reverse('index')
        self.assertRedirects(response, redirect_url)
        self.assertEquals(User.object.count(), 1)

    def test_register_error(self):
        data = {'username':'admin', 'password1': 'fulano159', 'password2': 'fulano159'}
        response = self.client.post(self.register_url, data)
        self.assertFormError(response, 'form', 'email', 'Este campo é obrigatório.')


class UpdateUserViewTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.update_url = reverse('accounts:update_user')
        self.user = mommy.prepare(settings.AUTH_USER_MODEL)
        self.user.set_password('123')
        self.user.save()

    def tearDown(self):
        self.user.delete()

    def test_update_user_ok(self):
        data = {'username': 'fulano', 'name': 'fulano de tal', 'email': 'fulano@admin.com'}
        response = self.client.get(self.update_url)
        self.assertEquals(response.status_code, 302)
        self.client.login(username=self.user.email, password='123')
        response = self.client.post(self.update_url, data)
        accounts_index_url = reverse('accounts:index')
        self.assertRedirects(response, accounts_index_url)
        self.user.refresh_from_db()
        self.assertEquals(self.user.email, 'fulano@admin.com')
        self.assertEquals(self.user.name, 'fulano de tal')

    def test_update_user_error(self):
        data = {}
        self.client.login(username=self.user.email, password='123')
        response = self.client.post(self.update_url, data)
        self.assertFormError(response, 'form', 'email', 'Este campo é obrigatório.')
        self.assertFormError(response, 'form', 'username', 'Este campo é obrigatório.')


class UpdatePasswordTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.update_url = reverse('accounts:update_password')
        self.user = mommy.prepare(settings.AUTH_USER_MODEL)
        self.user.set_password('123')
        self.user.save()

    def tearDown(self):
        self.user.delete()

    def test_update_password_ok(self):
        data = {'old_password': '123', 'new_password1': 'test123', 'new_password2': 'test123'}
        self.client.login(username=self.user.email, password='123')
        response = self.client.post(self.update_url, data)
        self.user.refresh_from_db()
        self.assertTrue(response, self.user.check_password('test123'))
