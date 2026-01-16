from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework import status
from django.urls import reverse
from .models import Employee


class EmployeeAPITest(APITestCase):

    def setUp(self):
        # Create test user
        self.user = User.objects.create_user(
            username="testuser",
            password="testpass123"
        )

        # Obtain JWT token
        token_response = self.client.post(
            reverse('token_obtain_pair'),
            {
                'username': 'testuser',
                'password': 'testpass123'
            },
            format='json'
        )

        self.assertEqual(
            token_response.status_code,
            status.HTTP_200_OK
        )

        self.access_token = token_response.data['access']

        # Attach token to every request
        self.client.credentials(
            HTTP_AUTHORIZATION=f'Bearer {self.access_token}'
        )

    # ---------------- CREATE ----------------
    def test_create_employee(self):
        response = self.client.post(
            reverse('employee-list'),
            {
                "name": "John",
                "email": "john@test.com"
            },
            format='json'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

    # ---------------- DUPLICATE EMAIL ----------------
    def test_duplicate_email(self):
        Employee.objects.create(
            name="John",
            email="john@test.com"
        )

        response = self.client.post(
            reverse('employee-list'),
            {
                "name": "Jane",
                "email": "john@test.com"
            },
            format='json'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )

    # ---------------- LIST ----------------
    def test_list_employees(self):
        Employee.objects.create(
            name="A",
            email="a@test.com"
        )

        response = self.client.get(
            reverse('employee-list')
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    # ---------------- RETRIEVE ----------------
    def test_get_employee(self):
        emp = Employee.objects.create(
            name="B",
            email="b@test.com"
        )

        response = self.client.get(
            reverse('employee-detail', args=[emp.id])
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    # ---------------- INVALID ID ----------------
    def test_invalid_employee(self):
        response = self.client.get(
            reverse('employee-detail', args=[999])
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_404_NOT_FOUND
        )

    # ---------------- DELETE ----------------
    def test_delete_employee(self):
        emp = Employee.objects.create(
            name="C",
            email="c@test.com"
        )

        response = self.client.delete(
            reverse('employee-detail', args=[emp.id])
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

    # ---------------- UNAUTHORIZED ----------------
    def test_unauthorized_access(self):
        self.client.credentials()  # remove token

        response = self.client.get(
            reverse('employee-list')
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_401_UNAUTHORIZED
        )




