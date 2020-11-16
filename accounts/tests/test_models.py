from django.test import TestCase
from accounts.models import User


class TestUserModels(TestCase):
    def setUp(self) -> None:
        self.user1 = User.objects.create(
            first_name='abc',
            last_name='xyz',
            is_employee=True,
            is_employer=False,
            user_gender='male',
            user_link='linkin.com',
            user_skills="python, java",
            email="abc@gmail.com",
            company_name="jobcom",
            company_address='pune',

        )

    def test_user_object(self):
        self.assertTrue(isinstance(self.user1, User))

    def test_unique_email(self):
        email = User(email='xyb@gmail.com').__unicode__()
        print(email)
        self.assertEqual(email, 'xyb@gmail.com')
