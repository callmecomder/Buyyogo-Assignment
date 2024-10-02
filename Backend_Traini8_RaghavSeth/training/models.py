# training/models.py
from django.db import models
from django.core.validators import RegexValidator, EmailValidator, MinLengthValidator
import time

class Address(models.Model):
    detailed_address = models.TextField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pincode = models.CharField(max_length=6)

class TrainingCenter(models.Model):
    center_name = models.CharField(max_length=40)
    center_code = models.CharField(max_length=12, unique=True)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    student_capacity = models.IntegerField(null=True, blank=True)
    courses_offered = models.JSONField()  # For list of courses
    created_on = models.DateTimeField(auto_now_add=True)
    contact_email = models.EmailField(null=True, blank=True)
    contact_phone = models.CharField(max_length=15)

    def __str__(self):
        return self.center_name
