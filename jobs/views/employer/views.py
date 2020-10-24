from django.views.generic import ListView, DetailView
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from jobs.models import Job, Applicant


class PostedJobs(LoginRequiredMixin, ListView):
    model = Job

    def get(self, request):
        context = []
        jobs = list(Job.objects.filter(user=self.request.user))
        jobs1 = Job.objects.filter(user=self.request.user)

        for _ in range(1+(len(jobs)//3)):
            lst = jobs[:3]
            del(jobs[:3])
            context.append(lst)

        return render(request, 'accounts/employer/posted-jobs.html', {'context':context, 'jobs':jobs1, 'posted_active':'active'})


class JobDetailsView(DetailView):
    model = Applicant

    def get(self, request, job_id):
        context = []
        job = Job.objects.filter(id=job_id).first()
        apps = list(self.model.objects.filter(job=job_id))

        # for _ in range(1+(len(apps)//3)):
        #     lst = apps[:3]
        #     del(apps[:3])
        #     context.append(lst)

        return render(request, 'jobs/details.html', {'context':apps, 'job':job})