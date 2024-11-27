from django.contrib import admin

# Register your models here.
from .models import Employee, Holiday

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'employee_id', 'department', 'work_location']
    search_fields = ['first_name', 'last_name', 'employee_id', 'department']


@admin.register(Holiday)
class HolidayAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'year')
    list_filter = ('year',)
    search_fields = ('name',)
    