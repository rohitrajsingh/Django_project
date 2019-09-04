from django import forms
from .models import Employee
class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['eno','ename','esal','eaddr','email','emess']

    def clean_email(self):
        email = self.cleaned_data.get("email")
        email_base,provider = email.split("@")
        domain,extension = provider.split(".")
        #if not domain =="usc":
        #   raise forms.ValidationError("Please make sure your USC email.")
        if not extension == "com":
            raise forms.ValidationError("Please use a valid .com email address")
        return email
    def clean_full_name(self):
        ename = self.cleaned_data.get("ename")
        return ename