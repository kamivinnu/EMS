"""
URL configuration for employee_management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from employees.views import employee_details, download_details, custom_login, user_profile, personal_details, account_details, work_experience, download_profile
from employees.views import CustomLoginView, holidays_calendar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', CustomLoginView.as_view(template_name='registration/login.html'), name='login'),
    # path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('employee/', employee_details, name='employee_details'),
    path('employee/download/', download_details, name='download_details'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # Logout view
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='registration/password_change.html'), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'), name='password_change_done'),
    path('login/', custom_login, name='login'),

    path('profile/', user_profile, name='user_profile'),
    path('personal-details/', personal_details, name='personal_details'),
    path('account-details/', account_details, name='account_details'),
    path('work-experience/', work_experience, name='work_experience'),
    path('download-profile/', download_profile, name='download_profile'),
    path('holidays-calendar/', holidays_calendar, name='holidays_calendar'),
]
