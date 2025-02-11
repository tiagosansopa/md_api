from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

class CustomUser(AbstractUser):
    
    DIMENSIONAL_UNIT_CHOICES = [
        ('cm', 'Centimeters'),
        ('m', 'Meters'),
        ('in', 'Inches'),
        ('ft', 'Feet'),
        ('kg', 'Kilograms'),
        ('lb', 'Pounds'),
    ]

    nickname = models.CharField(max_length=50, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10, blank=True)
    height = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)  # Value
    height_unit = models.CharField(max_length=2, choices=DIMENSIONAL_UNIT_CHOICES, default='cm')  # Unit
    weight = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)  # Value
    weight_unit = models.CharField(max_length=2, choices=DIMENSIONAL_UNIT_CHOICES, default='lb')  # Unit
    country = models.CharField(max_length=50, blank=True)
    disability = models.CharField(max_length=100, default='none')

    def __str__(self):
        return self.username
