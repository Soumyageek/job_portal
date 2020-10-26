from django.contrib.auth.models import AbstractUser
from django.db import models

from accounts.privilege import UserManagement

GENDER_CHOICES = (
    ('male', 'Male'),
    ('female', 'Female'))


class User(AbstractUser):
    username = None
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    # user_role = models.CharField(max_length=12, error_messages={
    #     'required': "please provide user role"
    # })
    is_employee = models.BooleanField(default=False)
    is_employer = models.BooleanField(default=False)
    user_gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    user_link = models.CharField(max_length=200, default="")
    user_skills = models.TextField(null=True, default="")
    email = models.EmailField(unique=True, blank=False,
                              error_messages={
                                  'unique': "A profile user with same email already exists in application.",
                              })

    company_name = models.CharField(max_length=20, default="")
    company_address = models.CharField(max_length=30, default="")
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __unicode__(self):
        return self.email

    objects = UserManagement()