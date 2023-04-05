from auth_app.api.serializers import RegisterSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework import status
#import serializers

#import httpResponse

from auth_app.models import Person


@api_view(['POST'])
@authentication_classes([TokenAuthentication])
def register(request):
    print(request.data.get('username'))
    person = Person.objects.filter(username=request.data.get('username'))
    if person:
        return Response("username already exists",status=400)
    else:
        serializer = RegisterSerializer(data=request.data)
        data = {}
       
        try:
            
            person1 = Person(username=request.data.get('username'),email=request.data.get('email'),password=request.data.get('password'))
            person1.save()
            # data['status'] = "Successfully registered a new user."
            # data['email'] = person.email
            # data['username'] = person.username
            # token = Token.objects.get(user=person).key
            # data['token'] = token
            return Response({'register success'},status=201)
        except ValueError as e:
            return Response({'error': str(e)},status=400)
       
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
    person_values = Person.objects.filter(username=request.user).values('username', 'email', 'is_admin')
    return Response(person_values)

@api_view(['GET'])
def all(request):
    person = Person.objects.all()
    print(person.values)
    return Response(person.values('username','email','password','is_admin'))

@api_view(['DELETE'])
def detete(request,staff_id):
    person = Person.objects.get(id=staff_id)
    person.delete()
    return Response("delete success")