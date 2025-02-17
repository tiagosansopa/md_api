from rest_framework import mixins, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth import get_user_model, authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserSerializer,RegisterSerializer

User = get_user_model()


class HealthCheckView(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        return Response({"message": "match day api up and running"}, status=status.HTTP_200_OK)
    
class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            return Response({
                "refresh": str(refresh),
                "access": str(refresh.access_token),
                "user": serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        email_or_username = request.data.get("email") or request.data.get("username")
        password = request.data.get("password")

        # Check if the input is an email or a username
        user = User.objects.filter(email=email_or_username).first() or \
               User.objects.filter(username=email_or_username).first()

        if user and user.check_password(password):
            refresh = RefreshToken.for_user(user)
            return Response({
                "refresh": str(refresh),
                "access": str(refresh.access_token),
                "user": UserSerializer(user).data
            }, status=status.HTTP_200_OK)

        return Response({"error": "Invalid credentials."}, status=status.HTTP_401_UNAUTHORIZED)

class CurrentUserView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data)
    
class UserViewSet(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_superuser:  # Allow admins to see all users
            return User.objects.all()
        return User.objects.filter(id=self.request.user.id)
