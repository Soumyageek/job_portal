from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from jobs.models import Job, Applicant
from  jobs.forms import CreateJobForm
from django.http import Http404


class IsUserEmployee(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_employee


class IsUserEmployer(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_employer


class PostedJobs(LoginRequiredMixin, ListView):
    model = Job

    def get(self, request):
        context = []
        jobs = list(Job.objects.filter(user=self.request.user))
        jobs1 = Job.objects.filter(user=self.request.user).order_by('-created_at')

        for _ in range(1+(len(jobs)//3)):
            lst = jobs[:3]
            del(jobs[:3])
            context.append(lst)

        return render(request, 'accounts/employer/posted-jobs.html', {'context':context, 'jobs':jobs1, 'posted_active':'active'})


class CreateJob(LoginRequiredMixin, IsUserEmployer, CreateView):
    model = Job
    form_class = CreateJobForm
    template_name = 'jobs/employee/create-job.html'
    success_url = 'jobs:posted-jobs'

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
            job.user = self.request.user
            job.save()
            messages.success(self.request, 'The job has been posted successfully.')
            return redirect('accounts:login')
        else:
            return render(request, 'jobs/employee/create-job.html', {'form': form, 'post_active':'active'})


class UpdateJob(LoginRequiredMixin, IsUserEmployer, UpdateView):
    model = Job
    form_class = CreateJobForm
    template_name = 'jobs/employee/create-job.html'
    success_url = 'jobs:posted-jobs'

    extra_context = {
        'title': 'Post a Job',
        'post_active': 'active'
    }

    # def dispatch(self, request, *args, **kwargs):
    #     if self.request.user.is_authenticated:
    #         return HttpResponseRedirect(self.get_success_url())
    #     return super().dispatch(self.request, *args, **kwargs)

    def get(self, request, job_id, *args):
        form = CreateJobForm(instance=Job.objects.get(id=job_id))
        return render(request, self.template_name, {'form':form, 'post_active':'active'})

    def post(self, request, job_id, *args, **kwargs):

        form = self.form_class(data=request.POST, instance=Job.objects.get(id=job_id))

        if form.is_valid():
            job = form.save(commit=False)
            job.user = self.request.user
            job.save()
            messages.success(self.request, 'The job has been updated successfully.')
            return redirect('accounts:login')
        else:
            return render(request, 'jobs/employee/create-job.html', {'form': form, 'post_active':'active'})


class DeleteJob(LoginRequiredMixin, IsUserEmployer, DeleteView):
    success_url = 'jobs:posted-jobs'

    def get(self, request, job_id):
        job = Job.objects.get(id=job_id)
        if job.user == self.request.user:
            messages.warning(self.request, 'The job has been deleted!')
            job.delete()
            return redirect('jobs:posted-jobs')
        else:
            raise Http404

class JobDetailsView(LoginRequiredMixin, DetailView):
    model = Applicant

    def get(self, request, job_id):
        context = []
        job = Job.objects.filter(id=job_id).first()
        apps = list(self.model.objects.filter(job=job_id).order_by('-score'))

        return render(request, 'jobs/details.html', {'apps':apps, 'job':job, 'applied_active':'active','posted_active':'active'})