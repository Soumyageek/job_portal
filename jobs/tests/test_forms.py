from django.forms import forms
from django.test import TestCase
from jobs.forms import CreateJobForm , ApplyJobForm , FileForm

class TestJobForm(TestCase):
    def setUp(self) -> None:
        self.form = CreateJobForm(
            data={
                'job_title': "Mahesh@94",
                'job_description': "male",
                'job_location': "pune",
                'type': "full time",
                'job_category': "python , java ",
                'last_date': "11/03/2021",
                'company_name': "noidecom",
                'company_description': "new ",
                'job_website': "likdin.com",
                'job_salary': "salary",

            }
        )
        self.form_update = ApplyJobForm(
        )
    def test_job_form(self):
        self.assertTrue(self.form.is_valid)

    def test_apply_form(self):
        self.assertTrue(self.form_update.is_valid)
