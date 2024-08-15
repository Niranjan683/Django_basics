#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'crudDemo.settings')
import django 
django.setup()

from crudApp.models import *
from faker import Faker
from random import *
faker= Faker()

def generate(n):
    for i in range(n):
        fstu_no=randint(1,1001)
        fstu_name=faker.name()
        fstu_class=randint(1,10)
        fstu_address=faker.city()
        emp_record=Student.objects.get_or_create(stu_no=fstu_no,stu_name=fstu_name,stu_class=fstu_class,stu_address=fstu_address)

generate(20)