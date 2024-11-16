from rest_framework import serializers
from .models import CustomUser
from .models import Discipline
from .models import Match, PlayerSlot

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'nickname', 'date_of_birth', 'gender', 'weight','weight_unit', 'height','height_unit','country','disability']

class DisciplineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discipline
        fields = ['id', 'name', 'favorite_position', 'dominant_foot', 'leader_number', 'clutch_number', 'pace', 'defending', 'shooting', 'passing', 'dribbling']

class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = ['id', 'place', 'date_time', 'player_count', 'formation']

class PlayerSlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayerSlot
        fields = ['slot_number', 'player', 'is_captain']

class MatchDetailSerializer(serializers.ModelSerializer):
    player_slots = PlayerSlotSerializer(many=True)

    class Meta:
        model = Match
        fields = ['id', 'place', 'location_coordinates', 'date_time', 'player_count', 'formation', 'field_type', 'player_slots']