from django.urls import path, include

from .views.home import SearchView
from .views.employer.views import PostedJobs, JobDetailsView, CreateJob
from .views.employee.views import ApplyJobView, AppliedJobs
from accounts.views import LoginView, landing_page

app_name = "jobs"

urlpatterns = [
    path('landing/', landing_page, name='landing'),
    path('', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('posted-jobs/', PostedJobs.as_view(), name='posted-jobs'),
    path('jobs/<int:job_id>/',JobDetailsView.as_view(), name='job-details'),
    path('search-jobs/', SearchView.as_view(), name='search-jobs'),
    path('post-job/', CreateJob.as_view(), name='post-job'),
    path('apply-job/<int:job_id>/', ApplyJobView.as_view(), name='apply-job'),
    path('applied-jobs/', AppliedJobs.as_view(), name='applied-jobs'),
]