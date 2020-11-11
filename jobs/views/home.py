from django.views.generic import ListView, DetailView, CreateView
from ..models import Job, Applicant
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from jobs.views.employer.views import IsUserEmployee


class SearchView(LoginRequiredMixin, ListView):
    model = Job
    template_name = 'jobs/search.html'
    context_object_name = 'jobs'
    extra_context = {'find_active': 'active'}
    paginate_by = 2

    def post(self, request):
        jobs = self.model.objects.filter(id=None)
        context = {'find_active': 'active', 'list_header': 'Jobs matching your search', 'jobs': jobs}
        print("hello ", jobs, "hello", request)
        if request.POST.get('location') or request.POST.get('position') or request.POST.get('category'):
            print(request.POST.get('category'))
            jobs = self.model.objects.filter(job_location__contains=self.request.POST['location'],
                                             job_title__contains=self.request.POST['position'],
                                             type__contains=self.request.POST['category']).order_by('-created_at')
            list_header = 'Jobs matching your search'
            applied_jobs = []
            other_jobs = []
            for job in jobs:
                if Applicant.objects.filter(job=job, user=request.user):
                    applied_jobs.append(job)
                else:
                    other_jobs.append(job)
            context = {'jobs': jobs, 'find_active': 'active',
                       'list_header': list_header, 'applied_jobs': applied_jobs, 'other_jobs': other_jobs}
        else:
            return redirect('jobs:search-jobs')
        return render(request, 'jobs/search.html', context)

    def get(self, request):
        context = {'find_active': 'active'}

        jobs = self.model.objects.all().order_by('-created_at')[:10]
        list_header = 'Jobs for you'
        applied_jobs = []
        other_jobs = []
        print("hello for get  ", jobs, "hello", request.POST.get('location'))
        context.update({'jobs': jobs, 'list_header': list_header, 'method': 'GET'})
        print("list_header", context)
        for job in jobs:
            if Applicant.objects.filter(job=job, user=request.user):
                applied_jobs.append(job)
            else:
                other_jobs.append(job)
        context = {'jobs': jobs, 'find_active': 'active',
                   'list_header': list_header, 'applied_jobs': applied_jobs, 'other_jobs': other_jobs}
        return render(request, 'jobs/search.html', context)
        # return render(request, 'jobs/search.html', context)
