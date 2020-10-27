from django.views.generic import ListView, DetailView, CreateView
from ..models import Job
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from jobs.views.employer.views import IsUserEmployee


class SearchView(LoginRequiredMixin, ListView):
    model = Job
    template_name = 'jobs/search.html'
    context_object_name = 'jobs'
    extra_context = {'find_active':'active'}
    paginate_by = 2

    def post(self, request):
        jobs = self.model.objects.filter(id=None)
        context = {'find_active':'active', 'list_header':'Jobs matching your search','jobs':jobs}
        if request.POST.get('location') or request.POST.get('position'):
            jobs = self.model.objects.filter(job_location__contains=self.request.POST['location'],
                                      job_title__contains=self.request.POST['position']).order_by('-created_at')
            list_header = 'Jobs matching your serch'
            context = {'jobs':jobs, 'find_active':'active', 'list_header':list_header}
        else:
            return redirect('jobs:search-jobs')
        return render(request, 'jobs/search.html', context)

    def get(self, request):
        context = {'find_active':'active'}
        jobs = self.model.objects.all().order_by('-created_at')[:10]
        list_header = 'Jobs for you'
        context.update({'jobs':jobs, 'list_header':list_header})
        return render(request, 'jobs/search.html', context)