from rest_framework import serializers
from .models import CustomUser, Discipline, Match, PlayerSlot

# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            'id', 'username', 'first_name', 'last_name', 'email', 
            'nickname', 'date_of_birth', 'gender', 
            'weight', 'weight_unit', 'height', 'height_unit', 
            'country', 'disability'
        ]

# Discipline Serializer
class DisciplineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discipline
        fields = [
            'id', 'name', 'favorite_position', 'dominant_foot', 
            'pace', 'defending', 'shooting', 'passing', 'dribbling', 
            'arm', 'chest', 'back', 'leg', 'strength', 'resistance', 
            'max_distance', 'pace_avg', 'level', 
            'forehand', 'backhand', 'tennis_level', 'created_at'
        ]

# Match Serializer
class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = [
            'id', 'place', 'location_coordinates', 'date_time', 
            'player_count', 'formation', 'field_type', 'creator'
        ]

# Player Slot Serializer
class PlayerSlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayerSlot
        fields = ['id', 'slot_number', 'player', 'is_captain', 'joined_at']

# Match Detail Serializer
class MatchDetailSerializer(serializers.ModelSerializer):
    player_slots = PlayerSlotSerializer(many=True)

    class Meta:
        model = Match
        fields = [
            'id', 'place', 'location_coordinates', 'date_time', 
            'player_count', 'formation', 'field_type', 'creator', 
            'player_slots'
        ]
