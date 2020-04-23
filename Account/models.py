from django.db import models
from django.contrib.auth.models import User

class Account(models.Model):
    phone = models.CharField(max_length=10)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class Owner(models.Model):
    shop_name = models.CharField(max_length=255)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class Employee(models.Model):
    department = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    owner_id = models.ForeignKey(Owner, on_delete=models.CASCADE)

    EMPLOYEE_TYPE_CHOICES = [
        ('PO', 'PURCHASING_OFFICER'),
        ('SO', 'SALE_OFFICER')
    ]
    employee_type = models.CharField(max_length=2, choices=EMPLOYEE_TYPE_CHOICES, null=False)
