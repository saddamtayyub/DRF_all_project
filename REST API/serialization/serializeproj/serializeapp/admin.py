from django.contrib import admin
from .models import Employees


# Register your models here.
@admin.register(Employees)
class EmpAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'emp_id', 'city']