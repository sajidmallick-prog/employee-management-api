from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework import status
from .models import Employee


class EmployeeAPITest(APITestCase):

    def setUp(self):
        # Create test user
        self.user = User.objects.create_user(
            username="testuser",
            password="testpass123"
        )

        # Get JWT token
        response = self.client.post('/api/token/', {
            'username': 'testuser',
            'password': 'testpass123'
        })

        self.access_token = response.data['access']

        # Attach token to every request
        self.client.credentials(
            HTTP_AUTHORIZATION='Bearer ' + self.access_token
        )


class EmployeeCreateTest(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            password="test123"
        )

        token_response = self.client.post('/api/token/', {
            'username': 'testuser',
            'password': 'test123'
        })

        self.token = token_response.data['access']
        self.client.credentials(
            HTTP_AUTHORIZATION='Bearer ' + self.token
        )

    def test_create_employee(self):
        response = self.client.post('/api/employees/', {
            "name": "John",
            "email": "john@test.com"
        })

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


    def test_duplicate_email(self):
        Employee.objects.create(
            name="John",
            email="john@test.com"
        )

        response = self.client.post('/api/employees/', {
            "name": "Jane",
            "email": "john@test.com"
        })

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )

    def test_list_employees(self):
        Employee.objects.create(
            name="A", email="a@test.com"
        )

        response = self.client.get('/api/employees/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_employee(self):
        emp = Employee.objects.create(
            name="B", email="b@test.com"
        )

        response = self.client.get(f'/api/employees/{emp.id}/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_employee(self):
        response = self.client.get('/api/employees/999/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


    def test_delete_employee(self):
        emp = Employee.objects.create(
            name="C", email="c@test.com"
        )

        response = self.client.delete(f'/api/employees/{emp.id}/')

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )


    def test_unauthorized_access(self):
        self.client.credentials()  # remove token

        response = self.client.get('/api/employees/')

        self.assertEqual(
            response.status_code,
            status.HTTP_401_UNAUTHORIZED
        )




