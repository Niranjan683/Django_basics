from django.db import models

# Create your models here.

class Student(models.Model):
    stu_no=models.IntegerField()
    stu_name=models.CharField(max_length=30)
    stu_class=models.IntegerField()
    stu_address=models.CharField(max_length=300) 