from django.db import models
from django.utils import timezone

from accounts.models import User

JOB_TYPE = (
    ('1', "Full Time"),
    ('2', "Part Time"),
    ('3', "Intern"),
)


class Job(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job_title = models.CharField(max_length=200)
    job_description = models.TextField()
    job_location = models.CharField(max_length=200)
    type = models.CharField(choices=JOB_TYPE, max_length=20)
    job_category = models.CharField(max_length=100)
    last_date = models.DateTimeField()
    company_name = models.CharField(max_length=100)
    company_description = models.CharField(max_length=300)
    job_website = models.CharField(max_length=200, default="")
    created_at = models.DateTimeField(default=timezone.now)
    filled = models.BooleanField(default=False)
    job_salary = models.BigIntegerField(default=0, blank=True)

    def __str__(self):
        return self.job_title


class Applicant(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='job_applicants')
    created_at = models.DateTimeField(default=timezone.now)
    score = models.IntegerField(default=0, blank=True, null=True)
    lor = models.FileField(default='lor.txt', upload_to='lor_docs')

    class Meta:
        unique_together = ['user', 'job']

    def __str__(self):
        return self.user.get_full_name()