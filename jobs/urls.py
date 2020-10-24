from django.urls import path, include

from .views.home import HomeView, SearchView
from .views.employer.views import PostedJobs, JobDetailsView

app_name = "jobs"

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('posted-jobs/', PostedJobs.as_view(), name='posted-jobs'),
    path('posted-jobs/<int:job_id>/',JobDetailsView.as_view(), name='job-app-details'),
    path('search-jobs/', SearchView.as_view(), name='search-jobs'),
]