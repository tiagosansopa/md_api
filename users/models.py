from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

class CustomUser(AbstractUser):
    DISABILITY_CHOICES = [
        ('none', 'None'),
        ('sight_impaired', 'Sight Impaired'),
        ('asthma', 'Asthma'),
        # Add more disabilities as needed
    ]
    
    DIMENSIONAL_UNIT_CHOICES = [
        ('cm', 'Centimeters'),
        ('m', 'Meters'),
        ('in', 'Inches'),
        ('kg', 'Kilograms'),
        ('lb', 'Pounds'),
    ]

    nickname = models.CharField(max_length=50, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10, blank=True)
    height = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)  # Value
    height_unit = models.CharField(max_length=2, choices=DIMENSIONAL_UNIT_CHOICES[:3], default='cm')  # Unit
    weight = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)  # Value
    weight_unit = models.CharField(max_length=2, choices=DIMENSIONAL_UNIT_CHOICES[3:], default='kg')  # Unit
    country = models.CharField(max_length=50, blank=True)
    disability = models.CharField(max_length=20, choices=DISABILITY_CHOICES, default='none')

    def __str__(self):
        return self.username
    



class Discipline(models.Model):
    DISCIPLINE_CHOICES = [
        ('soccer', 'Soccer'),
        ('running', 'Running'),
        ('gym', 'Gym'),
        # Add more disciplines as needed
    ]
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='disciplines')
    name = models.CharField(max_length=50, choices=DISCIPLINE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    # Soccer-specific fields
    favorite_position = models.CharField(max_length=50, blank=True, null=True)
    dominant_foot = models.CharField(max_length=10, choices=[('left', 'Left'), ('right', 'Right')], blank=True, null=True)
    leader_number = models.IntegerField(blank=True, null=True)
    clutch_number = models.IntegerField(blank=True, null=True)
    
    # Soccer stats
    pace = models.IntegerField(default=0)  # Ratings from 1 to 5
    defending = models.IntegerField(default=0)
    shooting = models.IntegerField(default=0)
    passing = models.IntegerField(default=0)
    dribbling = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.name.capitalize()} - {self.user.username}"

class Match(models.Model):
    FORMATION_CHOICES = [
        ('1', '1 Forward'),
        ('2', '2 Forwards'),
        ('3', '3 Forwards'),
    ]
    
    PLACE_TYPE_CHOICES = [
        ('outdoor', 'Outdoor'),
        ('indoor', 'Indoor'),
    ]

    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='created_matches')
    place = models.CharField(max_length=100)  # Name or description of the location
    location_coordinates = models.CharField(max_length=50, blank=True, null=True)  # Optional for coordinates
    date_time = models.DateTimeField()  # Date and time of the match
    player_count = models.IntegerField()  # Total number of players required
    formation = models.CharField(max_length=1, choices=FORMATION_CHOICES, default='1')
    field_type = models.CharField(max_length=10, choices=PLACE_TYPE_CHOICES, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.place} - {self.date_time.strftime('%Y-%m-%d %H:%M')}"

class PlayerSlot(models.Model):
    match = models.ForeignKey(Match, on_delete=models.CASCADE, related_name='player_slots')
    player = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    slot_number = models.IntegerField()  # Position on the field
    is_captain = models.BooleanField(default=False)
    joined_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Slot {self.slot_number} - {'Empty' if self.player is None else self.player.username}"
