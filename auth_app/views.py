from auth_app.api.serializers import RegisterSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
# import serializers

# import httpResponse

from auth_app.models import Person


@api_view(['POST'])
def register(request):
    serializer = RegisterSerializer(data=request.data)
    data = {}
    if serializer.is_valid():
        person = serializer.save()
        data['status'] = "Successfully registered a new user."
        data['email'] = person.email
        data['username'] = person.username
        token = Token.objects.get(user=person).key
        data['token'] = token
    else:
        data = serializer.errors
    return Response(data)


@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def logout(request):
    logout(request)
    return Response("logout success")


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def detail(request):
    print(request.user)
    person = Person.objects.get(username=request.user)
    print(person.is_admin)
    person_values = Person.objects.filter(
        username=request.user).values('username', 'email', 'is_admin')
    return Response(person_values)


@api_view(['GET'])
def all(request):
    person = Person.objects.all()
    print(person.values)
    return Response(person.values('username', 'email', 'password', 'is_admin'))
