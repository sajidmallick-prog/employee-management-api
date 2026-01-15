from django.shortcuts import render
from .models import Employee
from .serializers import EmployeeSerializers
from .pagination import EmployeePagination
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend



class EmployeeListCreateView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializers
    pagination_class = EmployeePagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['department', 'role']

class EmployeeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializers
    


