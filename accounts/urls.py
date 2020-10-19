from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from .views import *

# modules are included here
app_name = "accounts"

urlpatterns = [
    # URL for job seeker registration
    path('jobseeker/register', RegisterEmployeeView.as_view(), name='employee-register'),
    # URL for recruiter registration
    path('recruiter/register', RegisterEmployerView.as_view(), name='employer-register'),
    # Login and Log out path
    path('logout', LogoutView.as_view(), name='logout'),
    path('login', LoginView.as_view(), name='login'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
