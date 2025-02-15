from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RegisterView, LoginView, UserViewSet, CurrentUserView, HealthCheckView
from rest_framework_simplejwt.views import TokenRefreshView

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')  # Manages user retrieval, update, and delete

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"), 
    path("me/", CurrentUserView.as_view(), name="current-user"),  
    path("health/", HealthCheckView.as_view(), name="health"), 
    path("", include(router.urls)), 
]