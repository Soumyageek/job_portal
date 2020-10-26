from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from jobs.models import Job, Applicant
from  jobs.forms import CreateJobForm


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


class CreateJob(LoginRequiredMixin, CreateView):
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

        return render(request, 'jobs/details.html', {'apps':apps, 'job':job, 'applied_active':'active','posted_active':'active'})