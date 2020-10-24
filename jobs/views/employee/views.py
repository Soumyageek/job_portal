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

class CreateJob(LoginRequiredMixin, CreateView):
    model = Job
    form_class = CreateJobForm
    template_name = 'jobs/employee/create-job.html'
    success_url = '/'

    extra_context = {
        'title': 'Post a Job',
        'post_active': 'active'
    }

    # def dispatch(self, request, *args, **kwargs):
    #     if self.request.user.is_authenticated:
    #         return HttpResponseRedirect(self.get_success_url())
    #     return super().dispatch(self.request, *args, **kwargs)

    def get(self, request):
        form = CreateJobForm()
        return render(request, self.template_name, {'form':form, 'post_active':'active'})

    def post(self, request, *args, **kwargs):

        form = self.form_class(data=request.POST)

        if form.is_valid():
            job = form.save(commit=False)
            # if any fields need updation before saving
            job.user = self.request.user
            job.save()
            messages.success(request, 'The job has been posted successfully.')
            return redirect('accounts:login')
        else:
            return render(request, 'jobs/employee/create-job.html', {'form': form, 'post_active':'active'})


class AppliedJobs(View):
    model = Applicant
    def get(self, request):
        jobs = self.model.objects.filter(user=self.request.user)
        return render(request, 'jobs/jobs.html',{'jobs':jobs})


class ApplyJobView(CreateView):
    model = Applicant
    form_class = ApplyJobForm
    slug_field = 'job_id'
    slug_url_kwarg = 'job_id'

    @method_decorator(login_required(login_url=reverse_lazy('accounts:login')))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(self.request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            messages.info(self.request, 'Successfully applied for the job!')
            return self.form_valid(form)
        else:
            return HttpResponseRedirect(reverse_lazy('jobs:home'))

    def get_success_url(self):
        return reverse_lazy('jobs:job-details', kwargs={'job_id': self.kwargs['job_id']})

    # def get_form_kwargs(self):
    #     kwargs = super(ApplyJobView, self).get_form_kwargs()
    #     print(kwargs)
    #     kwargs['job'] = 1
    #     return kwargs

    def form_valid(self, form):
        # check if user already applied
        applicant = Applicant.objects.filter(user_id=self.request.user.id, job_id=self.kwargs['job_id'])
        if applicant:
            messages.info(self.request, 'You already applied for this job')
            return HttpResponseRedirect(self.get_success_url())
        # save applicant
        form.instance.user = self.request.user
        form.save()
        return super().form_valid(form)
