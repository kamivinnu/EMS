from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Link to Django user
    employee_name = models.CharField(max_length=100, blank=True, null=True)
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    gender = models.CharField(max_length=10)
    fathers_name = models.CharField(max_length=100)
    personal_email = models.EmailField()
    work_email = models.EmailField()
    mobile_number = models.CharField(max_length=15)
    date_of_joining = models.DateField()
    date_of_birth = models.DateField()
    age = models.IntegerField(blank=True, null=True)
    employment_type = models.CharField(max_length=50, blank=True, null=True)
    employee_id = models.CharField(max_length=20, unique=True)
    designation = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    work_location = models.CharField(max_length=100)
    enable_portal_access = models.BooleanField(default=False, blank=True, null=True)
    aadhar_card = models.CharField(max_length=20)
    pan = models.CharField(max_length=10, blank=True, null=True)
    residential_address = models.TextField(blank=True, null=True)
    pf_account_number = models.CharField(max_length=20)
    annual_ctc = models.DecimalField(max_digits=10, decimal_places=2)
    account_holder_name = models.CharField(max_length=100)
    bank_name = models.CharField(max_length=100)
    account_number = models.CharField(max_length=20)
    ifsc = models.CharField(max_length=11)
    account_type = models.CharField(max_length=20)
    total_work_experience = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    dat_work_experience = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    skill_set = models.TextField(blank=True, null=True)
    passport_number = models.CharField(max_length=20, default=True, null=True)
    passport_expiry_date = models.DateField(default=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.employee_id})"
    

class Holiday(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateField()
    year = models.IntegerField()

    class Meta:
        unique_together = ('name', 'date') # ensure no duplicate entries

    def __str__(self):
        return f"{self.name} ({self.date})"