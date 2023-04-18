from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.


class CustomUser(AbstractUser):
    email = models.CharField(max_length=255, unique=True)
    username = models.CharField(max_length=255, unique=True)
    mobile_number = PhoneNumberField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    password = models.CharField(max_length=255)
    age = models.IntegerField(null=True)
    number_of_dependents = models.IntegerField(null=True)
    monthly_income = models.FloatField(null=True)
    medical_conditions = models.TextField(null=True)
    permission_class = models.CharField(max_length=255, default='UNSUBSCRIBED')