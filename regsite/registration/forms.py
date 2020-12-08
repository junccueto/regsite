from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username']


class Step1Form(forms.Form):
    name = forms.CharField(label='Your Name', max_length=64)


class Step2Form(forms.Form):
    age = forms.IntegerField(label='Your Age')


class Step3Form(forms.Form):
    address = forms.CharField(label='City You Live In', max_length=256)