from django.contrib.auth.models import AbstractUser
from django.db import models

from accounts.privilege import UserManagement

GENDER_CHOICES = (
    ('male', 'MALE'),
    ('female', 'FEMALE'))


class User(AbstractUser):
    username = None
    user_role = models.CharField(max_length=12, error_messages={
        'required': "please provide user role"
    })
    user_gender = models.CharField(max_length=10, blank=True, null=True, default="")
    user_link = models.CharField(max_length=200, blank=True, null=True, default="")
    user_skills = models.TextField(null=True, default="")
    email = models.EmailField(unique=True, blank=False,
                              error_messages={
                                  'unique': "A profile user with same email already exists in application.",
                              })

    company_name = models.CharField(max_length=20, blank=True, null=True, default="")
    company_address = models.CharField(max_length=30, blank=True, null=True, default="")
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __unicode__(self):
        return self.email

    objects = UserManagement()







