from django.db import models

# Create your models here


class Department(models.Model):
    name = models.CharField(max_length=255, unique=True, null=False, blank=False)
    description = models.TextField(max_length=600 ,null=True, blank=True)

    def __str__(self):
        return self.name

class Employee(models.Model):
    first_name = models.CharField(max_length=60, null=False, blank=False)
    middle_name = models.CharField(max_length=60, null=True, blank=True)
    last_name = models.CharField(max_length=60, null=False, blank=False)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    

