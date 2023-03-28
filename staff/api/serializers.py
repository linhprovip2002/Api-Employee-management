from staff.models import Staff, attendance
from auth_app.models import Person
from rest_framework import serializers

class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = ('employee_code', 'first_name', 'last_name', 'phone', 'department', 'age', 'img', 'position')

class attendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = attendance
        fields = ('date', 'time_in', 'time_out', 'note')
class statisticalAttend(serializers.ModelSerializer):
    class Meta:
        model = attendance
        fields = ('date','employee_code', 'time_in', 'time_out', 'note')



