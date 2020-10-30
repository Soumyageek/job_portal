from django.views.generic import View, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from jobs.models import Job, Applicant
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse_lazy
from django.contrib import messages
from jobs.forms import CreateJobForm, ApplyJobForm
from ..employer.views import IsUserEmployee
from scraping import scrape_person


class AppliedJobs(LoginRequiredMixin, IsUserEmployee, View):
    model = Applicant
    def get(self, request):
        if request.user.is_employee:
            apps = self.model.objects.filter(user=self.request.user)
            jobs = []
            for job in apps:
                jobs.append(job.job)
            return render(request, 'accounts/employee/applied-jobs.html',{'jobs':jobs, 'applied_active':'active'})
        else:
            return redirect('jobs:landing')


class ApplyJobView(LoginRequiredMixin, IsUserEmployee, CreateView):
    model = Applicant

    def post(self, request, job_id):
        form = ApplyJobForm(data={'job':Job.objects.get(id=job_id), 'user':request.user})
        if form.is_valid():
            form.save()
            application=Applicant.objects.filter(job=Job.objects.get(id=job_id), user=request.user).first()
            score = scrape_person.get_score(skills_required = Job.objects.get(id=job_id).job_category, linkedin_url=request.user.user_link)
            application.score = score # Scraping and ML logic goes here.
            application.save()
            messages.success(request, 'You have successfully applied for this job.')
            return redirect('jobs:job-details', job_id=job_id)
        else:
            return redirect('jobs:job-details', job_id=job_id)