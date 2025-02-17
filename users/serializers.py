from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,  # Don't expose in API response
        required=True,
        # validators=[validate_password],  # Uses Django's password validation
        #style={'input_type': 'password'}  # UI hint for form rendering
    )

    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'password']

    def create(self, validated_data):
        """Handles user creation with hashed password"""
        user = User.objects.create_user(**validated_data)
        return user
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'nickname', 'gender']
        read_only_fields = ['email']  # Prevents email updates
 