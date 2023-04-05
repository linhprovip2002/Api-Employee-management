from auth_app.models import Person
from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError



class RegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    class Meta:
        model = Person
        fields = ['email', 'username', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True}
        }
    # def save(self):
    #     person = Person(
    #         email=self.validated_data['email'],
    #         username=self.validated_data['username'],
    #     )
    #     password = self.validated_data['password']
    #     password2 = self.validated_data['password2']
    #     try:
    #         validate_password(password=password, user=person)
    #     except ValidationError as e:
    #         raise serializers.ValidationError(e)
    #     if password != password2:
    #         raise serializers.ValidationError({'password': 'Passwords must match.'})
    #     person.set_password(password)
    #     person.save()
    #     return person  
