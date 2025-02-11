from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RegisterView, LoginView, UserViewSet, CurrentUserView, HealthCheckView
from rest_framework_simplejwt.views import TokenRefreshView

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')  # Manages user retrieval, update, and delete

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),  # User creation
    path("login/", LoginView.as_view(), name="login"),  # Login
    path("me/", CurrentUserView.as_view(), name="current-user"),  # Get logged-in user info
    path("health/", HealthCheckView.as_view(), name="health"),  # Get logged-in user info
    path("", include(router.urls)),  # Include UserViewSet routes
]