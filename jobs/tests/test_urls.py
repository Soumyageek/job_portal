from django.test import SimpleTestCase
from django.urls import reverse, resolve
# from accounts.views import RegisterEmployeeView, LogoutView, LoginView, RegisterEmployerView
from jobs.views.employee.views import AppliedJobs, ApplyJobView


class TestJobsUrls(SimpleTestCase):

    def test_landing_is_resolved(self):
        url = reverse('jobs:landing')
        print(resolve(url))
        self.assertTrue(resolve(url))

    def test_posted_jobs_url(self):
        url = reverse('jobs:posted-jobs')
        print(resolve(url))
        self.assertTrue(resolve(url))

    def test_post_jobs_url(self):
        url = reverse('jobs:post-job')
        print(resolve(url))
        self.assertTrue(resolve(url))

    def test_search_jobs_url(self):
        url = reverse('jobs:search-jobs')
        print(resolve(url))
        self.assertTrue(resolve(url))

    def test_applied_jobs_url(self):
        url = reverse('jobs:applied-jobs')
        print(resolve(url))
        self.assertTrue(resolve(url))

    def test_apply_jobs_url(self):
        url = reverse('jobs:apply-job',args=['1'])
        print(resolve(url))
        self.assertTrue(resolve(url))



