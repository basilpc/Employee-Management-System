from rest_framework import serializers

from employee.models import EmployeeField, Employee


# from .models import Employee, EmployeeField

class EmployeeFieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeField
        fields = ['id','field_name', 'field_value']

class EmployeeSerializer(serializers.ModelSerializer):
    custom_fields = EmployeeFieldSerializer(many=True)

    class Meta:
        model = Employee
        fields = ['id', 'name', 'email', 'position', 'custom_fields']

    def create(self, validated_data):
        custom_fields_data = validated_data.pop('custom_fields', [])
        employee = Employee.objects.create(**validated_data)
        for field_data in custom_fields_data:
            EmployeeField.objects.create(employee=employee, **field_data)
        return employee

    def update(self, instance, validated_data):
        custom_fields_data = validated_data.pop('custom_fields', [])
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.position = validated_data.get('position', instance.position)
        instance.save()

        for field_data in custom_fields_data:
            EmployeeField.objects.update_or_create(
                employee=instance,
                field_name=field_data.get('field_name'),
                defaults={'field_value': field_data.get('field_value')}
            )
        return instance