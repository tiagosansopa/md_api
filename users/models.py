from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    DISABILITY_CHOICES = [
        ('none', 'None'),
        ('sight_impaired', 'Sight Impaired'),
        ('asthma', 'Asthma'),
        # Add more disabilities as needed
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=50, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10, blank=True)  # Consider choices or other constraints if needed
    height = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)  # In cm or meters
    weight = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)  # In kg or lbs
    country = models.CharField(max_length=50, blank=True)
    disability = models.CharField(max_length=20, choices=DISABILITY_CHOICES, default='none')

    def __str__(self):
        return self.user.username