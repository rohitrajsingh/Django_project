'''from django.conf import smtplib
from django.core.mail import send_mail'''
from django.shortcuts import render
from .forms import EmployeeForm

# Create your views here.
from firstApp.models import Employee

def empdata(request):
    emp_list=Employee.objects.all()
    my_dict={'emp_list':emp_list}

    form = EmployeeForm()
    context = {
        "my_dict": my_dict,
        "form": form
    }
    return render(request, 'firstApp/emp.html', context=my_dict)
empdata='employee details'
mail = smtplibSMTP('smtp.gmail.com',587)
mail.ehlo()
mail.starttls()
mail.login('rohitrajsingh10@gmail.com','')
mail.sendmail('rohitrajsingh10@gmail.com','merohitraj01@gmail.com',empdata)







