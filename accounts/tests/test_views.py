from django.test import TestCase, Client, override_settings
from django.urls import reverse


class TestEmployeeRegisterView(TestCase):
    def setUp(self) -> None:
        self.client = Client()

    @override_settings(STATICFILES_STORAGE='django.contrib.staticfiles.storage.StaticFilesStorage')
    def test_post_register_employee(self):
        response = self.client.post(reverse('accounts:employee-register'))
        print(response.status_code)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response,'accounts/employee/register.html')
        response = self.client.patch(reverse('accounts:employee-register'))
        print(response.status_code)
        self.assertEquals(response.status_code, 405)
        # self.assertTemplateUsed(response, 'accounts/employee/register.html')

    @override_settings(STATICFILES_STORAGE='django.contrib.staticfiles.storage.StaticFilesStorage')
    def test_login_view(self):
        response = self.client.get(reverse('accounts:login'))
        self.assertEquals(response.status_code,200)
        # response = self.client.patch(reverse('accounts:login'))
        # self.assertEquals(response.status_code,200)

    @override_settings(STATICFILES_STORAGE='django.contrib.staticfiles.storage.StaticFilesStorage')
    def test_logout_view(self):
        response = self.client.get(reverse('accounts:logout'))
        self.assertEquals(response.status_code, 302)