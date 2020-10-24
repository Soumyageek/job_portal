from django.views.generic import View
from jobs.models import Job, Applicant

class AppliedJobs(View):
    model = Applicant
    def get(self, request):
        jobs = self.model.objects.filter(user=self.request.user)
