from django.forms import forms
from django.test import TestCase
from accounts.forms import EmployeeRegistrationForm, UserLoginForm, EmployerRegistrationForm, UpdateEmployerForm, \
    UpdateEmployeeForm


class TestEmployeeForm(TestCase):
    def setUp(self) -> None:
        self.form = EmployeeRegistrationForm(
            data={
                'password1': "Mahesh@94",
                'user_gender': "male",
                'first_name': "abc",
                'last_name': "xyz",
                'password2': "Mahesh@94",
                'user_link': "likdin.com",
                'email': "abc@gmail.com"
            }
        )
        self.form_update = UpdateEmployeeForm(
            data={
                'password1': "Mahesh@94",
                'user_gender': "male",
                'first_name': "abc",
                'last_name': "xyz",
                'password2': "Mahesh@94",
                'user_link': "likdin.com",
                'email': "abc@gmail.com"
            }
        )
    def test_employeeform(self):
        self.assertTrue(self.form.is_valid)

    def test_save_employeeform(self):
        self.assertTrue(self.form.save)

    def test_update_employeeform(self):
        self.assertTrue(self.form_update.is_valid)

    def test_update_save_employeeform(self):
        self.assertTrue(self.form_update.save)

    def test_clean_password1_employeeform(self):
        self.assertTrue(self.form_update.clean_password1)

    def test_clean_password2_employeeform(self):
        self.assertTrue(self.form_update.clean_password1)

    def test_userlogin_form(self):
        cred = UserLoginForm(data={'email': "abc@gmail.com", 'password': "Mahesh@94"})
        self.assertTrue(cred.clean)

class TestEmployerForm(TestCase):
    def setUp(self) -> None:
        self.form = EmployerRegistrationForm(
            data={
                'password1': "Mahesh@94",
                'company_name': "abc",
                'first_name': "abc",
                'last_name': "xyz",
                'password2': "Mahesh@94",
                'company_address': "likdin.com",
            }
        )
        self.form_update = UpdateEmployerForm(
            data={
                'password1': "Mahesh@94",
                'company_name': "abc",
                'first_name': "abc",
                'last_name': "xyz",
                'password2': "Mahesh@94",
                'company_address': "likdin.com",
            }
        )
    def test_employeeform(self):
        self.assertTrue(self.form.is_valid)

    def test_save_employeeform(self):
        self.assertTrue(self.form.save)

    def test_update_employeeform(self):
        self.assertTrue(self.form_update.is_valid)

    def test_save_update_employeeform(self):
        self.assertTrue(self.form_update.save)

    def test_clean_password1_employeeform(self):
        self.assertTrue(self.form_update.clean_password1)

    def test_clean_password2_employeeform(self):
        self.assertTrue(self.form_update.clean_password1)

