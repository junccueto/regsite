from django.urls import include, path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='login.html')),
    path('logout/', auth_views.LogoutView.as_view()),
    path('register/', views.Registration.as_view()),
    path('step1/', views.Step1.as_view()),
    path('step2/', views.Step2.as_view()),
    path('step3/', views.Step3.as_view()),
    path('inside/', views.Inside.as_view())
]
