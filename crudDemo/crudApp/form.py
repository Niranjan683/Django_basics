from django import forms
from crudApp.models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields='__all__'
        #exclude =['stu_no']       exclude is uused to remove the unwanted fields in the form