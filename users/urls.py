from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HealthCheckView,RegisterView, LoginView,UserViewSet, DisciplineViewSet, MatchViewSet,CurrentUserView,PlayerSlotViewSet
from rest_framework_simplejwt.views import TokenRefreshView

router = DefaultRouter()
router.register('player_slots', PlayerSlotViewSet, basename='player_slots')
router.register('users', UserViewSet, basename='user')
# router.register('user/<int:user_id>/disciplines', DisciplineViewSet, basename='discipline')
router.register('matches', MatchViewSet, basename='match')


discipline_list = DisciplineViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

discipline_detail = DisciplineViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = [
    path('health/', HealthCheckView.as_view(), name='health-check'),
    path('users/me/', CurrentUserView.as_view(), name='current-user'),
    path('user/<int:user_id>/disciplines/', discipline_list, name='discipline-list'),
    path('user/<int:user_id>/disciplines/<int:pk>/', discipline_detail, name='discipline-detail'),
    path('auth/register/', RegisterView.as_view(), name='register'),
    path('auth/login/', LoginView.as_view(), name='login'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include(router.urls)),
]

