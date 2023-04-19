from staff.models import Staff, attendance
from auth_app.models import Person
from rest_framework import serializers


class StaffSerializer(serializers.ModelSerializer):
    # id = serializers.IntegerField(source='person.id')
    class Meta:
        model = Staff
        fields = ('employee_code', 'first_name', 'last_name',
                  'phone', 'department', 'age', 'img', 'position', 'id')


class attendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = attendance
        fields = ('date', 'time_in', 'time_out', 'note')


class statisticalAttend(serializers.ModelSerializer):
    first_name = serializers.CharField(source='employee_code.first_name')
    last_name = serializers.CharField(source='employee_code.last_name')
    department = serializers.CharField(source='employee_code.department')
    position = serializers.CharField(source='employee_code.position')
    img = serializers.ImageField(source='employee_code.img')

    class Meta:
        model = attendance
        fields = ('date', 'employee_code', 'time_in', 'time_out', 'note',
                  'first_name', 'last_name', 'department', 'position', 'img')
