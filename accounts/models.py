from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import RegexValidator

from accounts.privilege import UserManagement

GENDER_CHOICES = (
    ('male', 'Male'),
    ('female', 'Female'))

alphabets = RegexValidator(r'^[a-zA-Z]*$', 'Numbers and Special Characters are not allowed!')


class User(AbstractUser):
    username = None
    first_name = models.CharField(max_length=20, validators=[alphabets])
    last_name = models.CharField(max_length=20, validators=[alphabets])
    # user_role = models.CharField(max_length=12, error_messages={
    #     'required': "please provide user role"
    # })
    is_employee = models.BooleanField(default=False)
    is_employer = models.BooleanField(default=False)
    user_gender = models.CharField(max_length=10, choices=GENDER_CHOICES, blank=True, null=True)
    user_link = models.CharField(max_length=200, default="")
    user_skills = models.TextField(null=True, default="")
    email = models.EmailField(unique=True, blank=False,
                              error_messages={
                                  'unique': "A profile user with same email already exists in application.",
                              })

    company_name = models.CharField(max_length=20, null=True, blank=True)
    company_address = models.CharField(max_length=30, null=True, blank=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __unicode__(self):
        return self.email

    objects = UserManagement()