from django.contrib import admin
from .models import SoccerPlayer, SoccerMatch, SoccerSlot, SoccerReview

admin.site.register(SoccerPlayer)
admin.site.register(SoccerMatch)
admin.site.register(SoccerSlot)
admin.site.register(SoccerReview)
