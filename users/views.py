from rest_framework.viewsets import ModelViewSet
from .models import CustomUser
from .models import Discipline
from .models import Match
from .serializers import UserSerializer
from .serializers import DisciplineSerializer
from .serializers import MatchSerializer
from .serializers import MatchDetailSerializer


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth import get_user_model, authenticate
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()


class HealthCheckView(APIView):
    def get(self, request):
        return Response({"message": "match day api up and running"}, status=status.HTTP_200_OK)

class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")
        username = request.data.get("username")

        if not email or not password:
            return Response({"error": "Email and password are required."}, status=status.HTTP_400_BAD_REQUEST)

        if User.objects.filter(email=email).exists():
            return Response({"error": "Email already in use."}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(email=email, password=password, username=username)

        refresh = RefreshToken.for_user(user)
        return Response({
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }, status=status.HTTP_201_CREATED)

class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response({
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            }, status=status.HTTP_200_OK)
        return Response({"error": "Invalid credentials."}, status=status.HTTP_401_UNAUTHORIZED)


class UserViewSet(ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        # Permite que el registro sea público, pero protege las demás acciones
        if self.action in ['create']:
            return [AllowAny()]
        return [IsAuthenticated()]
    

class DisciplineViewSet(ModelViewSet):
    serializer_class = DisciplineSerializer
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Filtra las disciplinas por el user_id en la URL
        user_id = self.kwargs.get('user_id')
        return Discipline.objects.filter(user_id=user_id)

    def perform_create(self, serializer):
        # Asocia automáticamente la disciplina al usuario especificado en la URL
        user_id = self.kwargs.get('user_id')
        serializer.save(user_id=user_id)


class MatchViewSet(ModelViewSet):
    queryset = Match.objects.all()
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        # Usa un serializer diferente para los detalles de un partido
        if self.action == 'retrieve':
            return MatchDetailSerializer
        return MatchSerializer

    def perform_create(self, serializer):
        # Asocia automáticamente el partido con el usuario autenticado
        serializer.save(creator=self.request.user)