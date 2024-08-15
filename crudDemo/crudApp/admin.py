from django.contrib import admin
from crudApp.models import Student

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list=['stu_no',' stu_name','stu_class','stu_address']
admin.site.register(Student,StudentAdmin)
