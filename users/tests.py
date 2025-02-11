from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()

class UserAPITestCase(APITestCase):
    def setUp(self):
        """Set up a test user before each test"""
        self.user = User.objects.create_user(
            email="test@example.com",
            username="testuser",
            password="TestPass123"
        )
        self.login_url = "/api/login/"
        self.register_url = "/api/register/"
        self.me_url = "/api/me/"
        self.user_detail_url = f"/api/users/{self.user.id}/"

    def test_register_user(self):
        """Test user registration"""
        data = {
            "email": "newuser@example.com",
            "username": "newuser",
            "password": "NewPass123"
        }
        response = self.client.post(self.register_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn("access", response.data)  # Check JWT is returned

    def test_login_user(self):
        """Test user login"""
        data = {
            "username": "testuser",
            "password": "TestPass123"
        }
        response = self.client.post(self.login_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("access", response.data)  # Check JWT is returned

    def test_invalid_login(self):
        """Test login with wrong password"""
        data = {
            "username": "testuser",
            "password": "WrongPass"
        }
        response = self.client.post(self.login_url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertIn("error", response.data)

    def test_get_current_user(self):
        """Test fetching the logged-in user's profile"""
        token = RefreshToken.for_user(self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token.access_token}')
        response = self.client.get(self.me_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["email"], self.user.email)

    def test_update_user_profile(self):
        """Test updating user profile"""
        token = RefreshToken.for_user(self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token.access_token}')
        update_data = {"nickname": "UpdatedNick"}
        response = self.client.patch(self.user_detail_url, update_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["nickname"], "UpdatedNick")

    def test_delete_user(self):
        """Test deleting a user"""
        token = RefreshToken.for_user(self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token.access_token}')
        response = self.client.delete(self.user_detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(User.objects.filter(email="test@example.com").exists())
