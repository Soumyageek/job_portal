from django.contrib import messages, auth
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import CreateView, FormView, RedirectView
from accounts.forms import *
from accounts.models import User
from jobs.views.employer.views import IsUserEmployer, IsUserEmployee
from django.contrib.auth.mixins import LoginRequiredMixin


class RegisterEmployeeView(CreateView):
    model = User
    form_class = EmployeeRegistrationForm
    template_name = 'accounts/employee/register1.html'
    success_url = '/'

    extra_context = {
        'title': 'Register',
        'register_active':'active'
    }

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        return super().dispatch(self.request, *args, **kwargs)

    def post(self, request, *args, **kwargs):

        form = self.form_class(data=request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data.get("password1")
            user.set_password(password)
            user.save()
            return redirect('accounts:login')
        else:
            return render(request, 'accounts/employee/register.html', {'form': form, 'update_active':'active'})



class UpdateEmployerView(LoginRequiredMixin, IsUserEmployer, FormView):
    model = User
    form_class = UpdateEmployerForm
    template_name = 'accounts/employer/update.html'
    success_url = '/'

    extra_context = {'update_active':'active',}

    def get(self, request):
        user = self.request.user
        form_class = self.form_class
        form = form_class(instance=user)
        return render(request, self.template_name, {'form': form, 'update_active':'active'})

    def post(self, request, *args, **kwargs):

        form = self.form_class(data=request.POST, instance=request.user)

        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            messages.success(request, 'The profile has been updated successfully!')
            return redirect('accounts:login')
        else:
            return render(request, self.template_name, {'form': form})


class UpdateEmployeeView(LoginRequiredMixin, IsUserEmployee, FormView):
    model = User
    form_class = UpdateEmployeeForm
    template_name = 'accounts/employee/update.html'
    success_url = '/'

    extra_context = {'update_active':'active'}


    def get(self, request):
        user = self.request.user
        form_class = self.form_class
        form = form_class(instance=user)
        return render(request, self.template_name, {'form': form, 'update_active':'active'})

    def post(self, request, *args, **kwargs):

        form = self.form_class(data=request.POST, instance=request.user)

        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            messages.success(request, 'The profile has been updated successfully!')
            return redirect('accounts:login')
        else:
            return render(request, self.template_name, {'form': form})


class RegisterEmployerView(CreateView):
    model = User
    form_class = EmployerRegistrationForm
    template_name = 'accounts/employer/register.html'
    success_url = '/'

    extra_context = {
        'title': 'Register',
        'register_active':'active'
    }

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        return super().dispatch(self.request, *args, **kwargs)

    def post(self, request, *args, **kwargs):

        form = self.form_class(data=request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data.get("password1")
            user.set_password(password)
            user.save()
            return redirect('accounts:login')
        else:
            return render(request, 'accounts/employer/register.html', {'form': form})


class LoginView(FormView):
    """
        Provides the ability to login as a user with an email and password
    """
    success_url = 'landing'
    form_class = UserLoginForm
    template_name = 'accounts/login.html'

    extra_context = {
        'title': 'Login'
    }

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        return super().dispatch(self.request, *args, **kwargs)

    def get_success_url(self):
        if 'next' in self.request.GET and self.request.GET['next'] != '':
            return self.request.GET['next']
        else:
            return self.success_url

    def get_form_class(self):
        return self.form_class

    def form_valid(self, form):
        auth.login(self.request, form.get_user())
        return redirect('/landing')

    def form_invalid(self, form):
        """If the form is invalid, render the invalid form."""
        return self.render_to_response(self.get_context_data(form=form))


class LogoutView(RedirectView):
    """
    Provides users the ability to logout
    """
    url = '/login'

    def get(self, request, *args, **kwargs):
        auth.logout(request)
        messages.success(request, 'You are now logged out')
        return super(LogoutView, self).get(request, *args, **kwargs)

def landing_page(request):
    if request.user.is_authenticated:
        if request.user.is_employee:
            return redirect('jobs:search-jobs')
        else:
            return redirect('jobs:posted-jobs')
    else:
        return redirect('accounts:login')