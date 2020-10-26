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


# class ApplyJobView(LoginRequiredMixin, CreateView):
#     model = Applicant
#     form_class = ApplyJobForm
#     slug_field = 'job_id'
#     slug_url_kwarg = 'job_id'
#
#     @method_decorator(login_required(login_url=reverse_lazy('accounts:login')))
#     def dispatch(self, request, *args, **kwargs):
#         return super().dispatch(self.request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         form = self.get_form()
#         if form.is_valid():
#             messages.info(self.request, 'Successfully applied for the job!')
#             return self.form_valid(form)
#         else:
#             return HttpResponseRedirect(reverse_lazy('jobs:home'))
#
#     def get_success_url(self):
#         return reverse_lazy('jobs:job-details', kwargs={'job_id': self.kwargs['job_id']})
#
#     # def get_form_kwargs(self):
#     #     kwargs = super(ApplyJobView, self).get_form_kwargs()
#     #     print(kwargs)
#     #     kwargs['job'] = 1
#     #     return kwargs
#
#     def form_valid(self, form):
#         # check if user already applied
#         applicant = Applicant.objects.filter(user_id=self.request.user.id, job_id=self.kwargs['job_id'])
#         if applicant:
#             messages.info(self.request, 'You already applied for this job')
#             return HttpResponseRedirect(self.get_success_url())
#         # save applicant
#         form.instance.user = self.request.user
#         form.save()
#         return super().form_valid(form)


class ApplyJobView(LoginRequiredMixin, IsUserEmployee, CreateView):
    model = Applicant

    def post(self, request, job_id):
        form = ApplyJobForm(data={'job':Job.objects.get(id=job_id), 'user':request.user})
        if form.is_valid():
            form.save()
            messages.success(request, 'You have successfully applied for this job.')
            return redirect('jobs:job-details/', job_id)
        else:
            return redirect('jobs:job-details/', job_id)