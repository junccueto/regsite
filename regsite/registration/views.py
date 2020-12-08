from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View

from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import UserProfile
from .forms import RegForm, Step1Form, Step2Form, Step3Form


class Registration(View):
    form_class = RegForm

    def get(self, request):
        form = self.form_class
        return render(request, template_name='register.html', context={'form':form})

    def post(self, request):
        form = self.form_class

        form_data = form(request.POST)

        if form_data.is_valid():
            user = form_data.save()
            profile = UserProfile(user=user)
            profile.save()

            username = form_data.cleaned_data.get('username')
            password = form_data.cleaned_data.get('password1')
            auth_user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/step1/')

        else:
            error_msg = 'Invalid Data Input.'
            return render(request, template_name='register.html',
                            context={'form':form,'error':error_msg})


class Step1(LoginRequiredMixin, View):
    form_class = Step1Form

    def get(self, request):
        form = self.form_class
        return render(request, template_name='step1.html', context={'form':form})

    def post(self, request):
        form = self.form_class

        form_data = form(request.POST)

        if form_data.is_valid():
            profile = UserProfile.objects.get(user=request.user)
            profile.name = form_data.cleaned_data.get('name')
            profile.save()

            return redirect('/step2/')
        else:
            error_msg = 'Invalid Data Input.'
            return render(request, template_name='step1.html',
                            context={'form':form,'error':error_msg})


class Step2(LoginRequiredMixin, View):
    form_class = Step2Form

    def get(self, request):
        user = request.user
        profile = UserProfile.objects.get(user=user)

        if profile.name:
            form = self.form_class
            return render(request, template_name='step2.html', context={'form':form})
        else:
            return redirect('/step1/')

    def post(self, request):
        form = self.form_class

        form_data = form(request.POST)

        if form_data.is_valid():
            profile = UserProfile.objects.get(user=request.user)
            profile.age = form_data.cleaned_data.get('age')
            profile.save()

            return redirect('/step3/')
        else:
            error_msg = 'Invalid Data Input.'
            return render(request, template_name='step2.html',
                            context={'form':form,'error':error_msg})


class Step3(LoginRequiredMixin, View):
    form_class = Step3Form

    def get(self, request):
        user = request.user
        profile = UserProfile.objects.get(user=user)

        if profile.age:
            form = self.form_class
            return render(request, template_name='step3.html', context={'form':form})
        else:
            return redirect('/step2/')

    def post(self, request):
        form = self.form_class

        form_data = form(request.POST)

        if form_data.is_valid():
            profile = UserProfile.objects.get(user=request.user)
            profile.address = form_data.cleaned_data.get('address')
            profile.save()

            return redirect('/inside/')
        else:
            error_msg = 'Invalid Data Input.'
            return render(request, template_name='step3.html',
                            context={'form':form,'error':error_msg})


class Inside(LoginRequiredMixin, View):

    def get(self, request):
        profile = UserProfile.objects.get(user=request.user)

        if profile.name is None:
            return redirect('/step1/')
        elif profile.age is None:
            return redirect('/step2/')
        elif profile.address is None:
            return redirect('/step3/')
        else:
            return render(request, template_name='inside.html', context={'info':profile})