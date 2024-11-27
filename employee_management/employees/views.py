from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Employee, Holiday
from django.http import HttpResponse
import pandas as pd
from django.contrib import messages  # Add this to display messages

from django.contrib.auth import authenticate, login
# from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm

from django.contrib.auth.views import LoginView
from .forms import CustomLoginForm

from django.utils import timezone

@login_required
def employee_details(request):
    try:
        employee = Employee.objects.get(user=request.user)
        return render(request, 'user_profile.html', {'employee': employee})
    except Employee.DoesNotExist:
        return HttpResponse("No employee data found for this user", status=404)

@login_required
def download_details(request):
    try:
        employee = Employee.objects.get(user=request.user)
        # Convert employee data to a dictionary
        employee_data = {
            'Employee Name': employee.employee_name,
            
            'First Name': employee.first_name,
            'Middle Name': employee.middle_name,
            'Last Name': employee.last_name,
            'Gender': employee.gender,
            'Father\'s Name': employee.fathers_name,
            'Personal Email': employee.personal_email,
            'Work Email': employee.work_email,
            'Mobile Number': employee.mobile_number,
            'Date of Joining': employee.date_of_joining,
            'Date of Birth': employee.date_of_birth,
            'Age': employee.age,
            'Employment Type': employee.employment_type,
            'Employee ID': employee.employee_id,
            'Designation': employee.designation,
            'Department': employee.department,
            'Work Location': employee.work_location,
            'Enable Portal Access': employee.enable_portal_access,
            'Aadhar Card': employee.aadhar_card,
            'PAN': employee.pan,
            'Residential Address': employee.residential_address,
            'PF Account Number': employee.pf_account_number,
            'Annual CTC': employee.annual_ctc,
            'Account Holder Name': employee.account_holder_name,
            'Bank Name': employee.bank_name,
            'Account Number': employee.account_number,
            'IFSC': employee.ifsc,
            'Account Type': employee.account_type,
            'Total Work Experience': employee.total_work_experience,
            'DAT Work Experience': employee.dat_work_experience,
            'Skill Set': employee.skill_set,
            'Passport Number': employee.passport_number,
            'Passport Expiry Date': employee.passport_expiry_date,
            # Add all other fields as necessary
        }

        df = pd.DataFrame([employee_data])

        # Convert DataFrame to Excel
        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = f'attachment; filename=employee_{employee.employee_id}.xlsx'
        df.to_excel(response, index=False)
        return response
    except Employee.DoesNotExist:
        return HttpResponse("No employee data found for this user", status=404)




def custom_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                
                # Check if "Remember Me" was checked
                if request.POST.get('remember_me'):
                    request.session.set_expiry(1209600)  # 2 weeks in seconds
                else:
                    request.session.set_expiry(0)  # Browser close will log out the user

                return redirect('user_profile')  # Redirect to employee details page
            else:
                messages.error(request, 'Invalid username or password')  # Display error message
        else:
            messages.error(request, 'Invalid username or password')  # Display error message

    else:
        form = AuthenticationForm()

    return render(request, 'registration/login.html', {'form': form})



def user_profile(request):
    employee = Employee.objects.get(user=request.user)
    return render(request, 'user_profile.html', {'employee': employee})

def personal_details(request):
    employee = Employee.objects.get(user=request.user)
    return render(request, 'personal_details.html', {'employee': employee})

def account_details(request):
    employee = Employee.objects.get(user=request.user)
    return render(request, 'account_details.html', {'employee': employee})

def work_experience(request):
    employee = Employee.objects.get(user=request.user)
    return render(request, 'work_experience.html', {'employee': employee})

def download_profile(request):
    employee = Employee.objects.get(user=request.user)
    # Code to download profile as XLSX
    return render(request, 'download_profile.html')

class CustomLoginView(LoginView):
    form_class = CustomLoginForm
    template_name = 'login.html'

def holidays_calendar(request):
    current_year = timezone.now().year

    selected_year = request.GET.get('year', current_year)

    # Fetch holidays for the selected year
    holidays = Holiday.objects.filter(year=selected_year).order_by('date')

    # holidays = Holiday.objects.filter(year=current_year)

     # Pass the available years (you can manually define or extract from database)
    # available_years = [2023, 2024, 2025]  # You can update this list as needed
    available_years = Holiday.objects.values_list('year', flat=True).distinct()
    
    context = {
        'holidays': holidays,
        'selected_year': selected_year,
        'available_years': available_years,
        'username': request.user.username,  # To display username in the dashboard
    }
    return render(request, 'holidays_calendar.html', context)