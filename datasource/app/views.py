from django.shortcuts import render
from rest_framework.views import APIView
from .models import Department, Employee
from .serializers import DepartmentSerializer, EmployeeSerializer
from rest_framework import status
from rest_framework.response import Response


class DepartmentView(APIView):
    def get(self, request):
        output = [{'name': output.name, 'description': output.description} for output in Department.objects.all()]
        return Response(output)
    
    def post(self, request):
        serializer = DepartmentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            # Print validation errors to debug
            print(serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class EmployeeView(APIView):
    def get(self, request):
        output = [{'first_name': output.first_name, 'middle_name': output.middle_name, 'last_name': output.last_name, 'department': output.department.name} for output in Employee.objects.all()]
        return Response(output)
    
    def post(self, request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
