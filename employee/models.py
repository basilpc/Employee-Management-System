from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    position = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class EmployeeField(models.Model):
    employee = models.ForeignKey(Employee, related_name='custom_fields', on_delete=models.CASCADE)
    field_name = models.CharField(max_length=100)
    field_value = models.TextField()

    def __str__(self):
        return f"{self.field_name}: {self.field_value}"