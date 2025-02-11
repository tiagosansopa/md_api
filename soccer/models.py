from django.db import models
from django.conf import settings

class SoccerPlayer(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="soccer_profile")
    dominant_foot = models.CharField(max_length=10, choices=[('left', 'Left'), ('right', 'Right'), ('both', 'Both')])
    position = models.CharField(max_length=50, choices=[
        ('goalkeeper', 'Goalkeeper'),
        ('defender', 'Defender'),
        ('midfielder', 'Midfielder'),
        ('forward', 'Forward'),
    ])
    porteria = models.IntegerField(default=1)
    velocidad = models.IntegerField(default=1)
    defensa = models.IntegerField(default=1)
    disparo = models.IntegerField(default=1)
    pase = models.IntegerField(default=1)
    regate = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.user.nickname} - {self.position}"


class SoccerMatch(models.Model):
    FORMATION_CHOICES = [
        ('1', '1 Forward'),
        ('2', '2 Forwards'),
        ('3', '3 Forwards'),
    ]

    PLACE_TYPE_CHOICES = [
        ('outdoor', 'Outdoor'),
        ('indoor', 'Indoor'),
    ]

    location = models.CharField(max_length=255)
    date_time = models.DateTimeField()
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="created_soccer_matches")
    players = models.ManyToManyField(SoccerPlayer, through='SoccerSlot', related_name="matches")
    formation = models.CharField(max_length=1, choices=FORMATION_CHOICES, default='1')
    bench_size = models.IntegerField(default=1)
    field_type = models.CharField(max_length=10, choices=PLACE_TYPE_CHOICES, blank=True, null=True)

    def __str__(self):
        return f"Match at {self.location} on {self.date_time}"
#       return f"{self.place} - {self.date_time.strftime('%Y-%m-%d %H:%M')}"


class SoccerSlot(models.Model):
    match = models.ForeignKey(SoccerMatch, on_delete=models.CASCADE, related_name="slots")
    player = models.ForeignKey(SoccerPlayer, on_delete=models.SET_NULL, null=True, blank=True, related_name="slots")
    position = models.CharField(max_length=50)  # Position in formation (e.g., "Left Midfielder")
    slot_number = models.IntegerField()
    joined_at = models.DateTimeField(auto_now_add=True)
    team = models.IntegerField(null=True, blank=True)
    def __str__(self):
        return f"{self.position} in {self.match}"
#       return f"Slot {self.slot_number} - {'Empty' if self.player is None else self.player.username}"


class SoccerReview(models.Model):
    match = models.ForeignKey(SoccerMatch, on_delete=models.CASCADE, related_name="reviews")
    reviewer = models.ForeignKey(SoccerPlayer, on_delete=models.CASCADE, related_name="given_reviews")
    reviewed_player = models.ForeignKey(SoccerPlayer, on_delete=models.CASCADE, related_name="received_reviews")
    rating = models.IntegerField(default=1) 
    comments = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.reviewer} reviewed {self.reviewed_player} for {self.match}"
