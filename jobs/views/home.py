from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView, CreateView
from ..models import Job
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from jobs.views.employer.views import IsUserEmployee


class HomeView(LoginRequiredMixin, ListView):
    model = Job
    template_name = 'home.html'
    context_object_name = 'jobs'

    def get_queryset(self):
        return self.model.objects.all()[:6]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['trendings'] = self.model.objects.filter(created_at__month=timezone.now().month)[:3]
        context['home_active'] = 'active'
        return context


class SearchView(LoginRequiredMixin, ListView):
    model = Job
    template_name = 'jobs/search.html'
    context_object_name = 'jobs'
    extra_context = {'find_active':'active'}
    paginate_by = 2

    def post(self, request):
        jobs = self.model.objects.filter(id=7238913)
        context = {'find_active':'active', 'list_header':'Jobs matching your search','jobs':jobs}
        if request.POST.get('location') or request.POST.get('position'):
            jobs = self.model.objects.filter(job_location__contains=self.request.POST['location'],
                                      job_title__contains=self.request.POST['position']).order_by('-created_at')
            list_header = 'Jobs matching your serch'
            context = {'jobs':jobs, 'find_active':'active', 'list_header':list_header}
        return render(request, 'jobs/search.html', context)

    def get(self, request):
        context = {'find_active':'active'}
        jobs = self.model.objects.all().order_by('-created_at')[:10]
        list_header = 'Jobs for you'
        context.update({'jobs':jobs, 'list_header':list_header})
        return render(request, 'jobs/search.html', context)