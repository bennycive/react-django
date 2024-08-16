from django.urls import path
from .views import DepartmentView, EmployeeView

urlpatterns = [
    path('departments/', DepartmentView.as_view(), name='department-list'),
    path('employees/', EmployeeView.as_view(), name='employee-list'),
]
