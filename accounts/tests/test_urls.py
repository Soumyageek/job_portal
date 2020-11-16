from django.test import SimpleTestCase
from django.urls import reverse, resolve
from accounts.views import RegisterEmployeeView, LogoutView, LoginView, RegisterEmployerView


class TestUrls(SimpleTestCase):

    def test_employee_url_is_resolved(self):
        url = reverse('accounts:employee-register')
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, RegisterEmployeeView)

    def test_employer_url_is_resolved(self):
        url = reverse('accounts:employer-register')
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, RegisterEmployerView)

    def test_login_url_is_resolved(self):
        url = reverse('accounts:login')
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, LoginView)

    def test_logout_url_is_resolved(self):
        url = reverse('accounts:logout')
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, LogoutView)


