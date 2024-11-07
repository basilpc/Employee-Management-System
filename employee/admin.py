from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Employee, EmployeeField

class EmployeeFieldInline(admin.TabularInline):
    model = EmployeeField
    extra = 1

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'position')
    inlines = [EmployeeFieldInline]