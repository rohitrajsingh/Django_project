from django.contrib import admin

# Register your models here.
from .forms import EmployeeForm
from firstApp.models import Employee

class EmployeeAdmin(admin.ModelAdmin):
    list_display=['eno','ename','esal','eaddr','email','emess',]
    form = EmployeeForm

admin.site.register(Employee,EmployeeAdmin)
