from auth_app.api.serializers import RegisterSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework import status
# import serializers

# import httpResponse

from auth_app.models import Person


@api_view(['POST'])
def login(request):
    try:
        person = Person.objects.get(username=request.data.get('username'))
        if person.check_password(request.data.get('password')):
            token, created = Token.objects.get_or_create(user=person)
            data = {
                'status': 'Successfully logged in user.',
                'email': person.email,
                'username': person.username,
                'id': person.id,
                'token': token.key
            }
            return Response(data)
        else:
            errors = "Incorrect password"
            return Response(errors, status=status.HTTP_400_BAD_REQUEST)
    except:
        errors = "User is not existed"
        return Response(errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def register(request):

    # serializer = RegisterSerializer(data=request.data)
    # if serializer.is_valid():
    #     person = Person(email =request.data.get('email'),username= request.data.get('username'),password= request.data.get('password'))
    #     person.set_password(request.data.get('password'))
    #     person.save()

    #     return Response("register success")
    # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    serializer = RegisterSerializer(data=request.data)
    print(serializer)
    print(serializer.is_valid())
    if serializer.is_valid():
        person = serializer.save()
        token, created = Token.objects.get_or_create(user=person)
        data = {
            'status': 'Successfully registered a new user.',
            'email': person.email,
            'username': person.username,
            'token': token.key
        }
        return Response(data)
    else:
        errors = "User is already existed"
        return Response(errors, status=status.HTTP_400_BAD_REQUEST)


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
    return Response(person.values('username', 'email', 'password', 'is_admin', 'id'))


@api_view(['DELETE'])
def detete(request, staff_id):
    print("delete ne")
    person = Person.objects.get(id=staff_id)
    person.delete()
    return Response("delete success")
