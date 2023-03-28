from staff.models import Staff,attendance
from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated,AllowAny
from django.http import HttpResponse
from rest_framework.response import Response
from staff.api.serializers import StaffSerializer,attendanceSerializer
from auth_app.models import Person
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def create(request):
    print(request.user)
    staff = Staff(id = request.user)
    serializer = StaffSerializer(staff,data=request.data)
    print(serializer)
    if serializer.is_valid():
        serializer.save()
        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )
    else:
        return Response(serializer.errors)

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
def get_detail_staff(request,staff_id):
    print(request.user)
    staff = Staff.objects.get(employee_code = staff_id)
    serializer = StaffSerializer(staff)
    return Response(serializer.data)
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
def get_all_staff(request):
    staff = Staff.objects.all()
    serializer = StaffSerializer(staff,many=True)
    return Response(serializer.data)

@api_view(['PUT'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def update_staff(request,staff_id):
        staff = Staff.objects.get(employee_code=staff_id)
        person = Person.objects.get(username=request.user)
        if person.is_admin == False:
            return Response("you not have admin permission",status=status.HTTP_401_UNAUTHORIZED)
        else:
            serializer = StaffSerializer(staff,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    serializer.data,
                    status=status.HTTP_200_OK
                )
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
@api_view(['DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def delete_staff(request,staff_id):
        staff = Staff.objects.get(employee_code=staff_id)
        person = Person.objects.get(username=request.user)
        if person.is_admin == False:
            return Response("you not have admin permission",status=status.HTTP_401_UNAUTHORIZED)
        else:
            staff.delete()
            return Response("delete success",status=status.HTTP_200_OK)        

# class StaffViewSet(viewsets.ModelViewSet):
#     queryset = Staff.objects.all()
#     permission_classes = [IsAuthenticated]
#     serializer_class = StaffSerializer
    
#     def create(self,request):
#             # person = Person()            
#             # #person.save()
#             # serializer = StaffSerializer(data=request.data)
#             # #print(serializer)
#             # data = {}
#             # if serializer.is_valid():
#             #     staff = serializer.save(person = person)
#             #     data['status'] = "Successfully update a user."
#             #     data['employee_code']= staff.employee_code
#             #     data['first_name'] = staff.first_name
#             #     data['last_name'] = staff.last_name
#             #     data['number_phone'] = staff.number_phone
#             #     data['department'] = staff.department
#             #     data['age'] = staff.age
#             #     data['sex'] = staff.sex
#             #     data['img'] = staff.img
#             #     data['address'] = staff.address
#             #     data['id'] = staff.id
#             # else:
#             #     data = serializer.errors
#             # return Response(data)        


#             print(request.user)
            
#             staff = Staff(id = request.user)
#             serializer = StaffSerializer(staff,data=request.data)
#             print(serializer)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(
#                     serializer.data,
#                     status=status.HTTP_200_OK
#                 )
#             else:
#                 return Response(serializer.errors)
#             # person = Person.objects.get(request.user)
#             # print(person.is_admin)
#             # if(person.is_admin == False):
#             #     return Response("you not have admin permission")
#             # else:
#             #     serializer = StaffSerializer(person,data=request.data)            
#             #     if serializer.is_valid():
#             #         serializer.save()
#             #         return Response(
#             #         serializer.data,
#             #         status=status.HTTP_200_OK
#             #     )
#             #     print(serializer.errors)
#             #     return Response("false update")

# from rest_framework.views import APIView
# class StaffDetailView(APIView):
#     serializer_class = StaffSerializer
#     def get(self, request, staff_id):
#         staff = Staff.objects.get(employee_code=staff_id)
#         serializer = StaffSerializer(staff)
#         #print(serializer)
#         # Perform any additional logic here
#         return Response(serializer.data)
    
#     def put(self,request,staff_id):
#         staff = Staff.objects.get(employee_code=staff_id)
#         person = Person.objects.get(username=request.user)
#         if person.is_admin == False:
#             return Response("you not have admin permission",status=status.HTTP_401_UNAUTHORIZED)
#         else:
#             serializer = StaffSerializer(staff,data=request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(
#                     serializer.data,
#                     status=status.HTTP_200_OK
#                 )
#             return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
#     def delete(self,request,staff_id):
#         person = Person.objects.get(username=request.user)
#         if person.is_admin == False:
#             return Response("you not have admin permission")
#         else:
#             staff = Staff.objects.get(employee_code=staff_id)
#             staff.delete()
#             return Response("delete success",status=status.HTTP_204_NO_CONTENT)
#     permission_classes = [IsAuthenticated]      
# from datetime import datetime
# class AttendanceViewSet(viewsets.ModelViewSet):
#     permission_classes = [IsAuthenticated]
#     serializer_class = attendanceSerializer
#     def create_time_in(self, request, staff_id):
#         data_attend={
#             "date":datetime.now(),
#             "time_in":datetime.now().time(),
#             "note":"test"
#         }
#         staff = Staff.objects.get(employee_code=staff_id)
#         print(staff)
#         attend = attendance(employee_code=staff)
#         serializer = attendanceSerializer(attend,data=data_attend)
#         # attends = attendance.objects.filter(employee_code=staff_id)
#         # print(attends.values())
#         if serializer.is_valid():
#                 serializer.save()
#                 return Response(
#                     serializer.data,
#                     status=status.HTTP_200_OK
#                 )
#         else:
#                 return Response(serializer.errors)
        
#         # attend = attendance(employee_code=staff)

        
       
#         # serializer = attendanceSerializer(attend,data=data_attend)
#         # print(serializer)
#         # if serializer.is_valid():
#         #     serializer.save()
#         #     return Response(
#         #         serializer.data,
#         #         status=status.HTTP_200_OK
#         #     )
#         # else:
#         #     return Response(serializer.errors)
        

        
#     # def list(self,request):
#     #     attend = attendance.objects.all()
#     #     serializer = StaffSerializer(attend,many=True)
#     #     return Response(serializer.data)
#     # def retrieve(self,request,pk=None):
#     #     attend = attendance.objects.get(id=pk)
#     #     serializer = StaffSerializer(attend)
#     #     return Response(serializer.data)
#     # def update(self,request,pk=None):
#     #     attend = attendance.objects.get(id=pk)
#     #     serializer = StaffSerializer(attend,data=request.data)
#     #     if serializer.is_valid():
#     #         serializer.save()
#     #         return Response(
#     #             serializer.data,
#     #             status=status.HTTP_200_OK
#     #         )
#     #     return Response("false update")
#     # def destroy(self,request,pk=None):
#     #     attend = attendance.objects.get(id=pk)
#     #     attend.delete()
#     #     return Response("delete success")    

# # class attend_statistical(APIView):
# #     permission_classes = [IsAuthenticated]
# #     serializer_class = StaffSerializer
# #     def getday(self,request):
# #         params = request.GET
# #         day = params.get('day')
# #         attend = attendance.objects.all()

# #         serializer = StaffSerializer(attend,many=True)
# #         return Response(serializer.data)
from datetime import datetime
@api_view(['POST'])

def create_time_in(request,staff_id):
    data_attend={
            "date":datetime.now(),
            "time_in":datetime.now().time(),
            "note":"test"
        }
    staff = Staff.objects.get(employee_code=staff_id)
    print(staff)
    attend = attendance(employee_code=staff)
    serializer = attendanceSerializer(attend,data=data_attend)
    # attends = attendance.objects.filter(employee_code=staff_id)
    # print(attends.values())
    if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_200_OK
            )
    else:
            return Response(serializer.errors)
    
    # attend = attendance(employee_code=staff)
@api_view(['PUT'])
def update_time_out(request,staff_id):
    data_attend={
            "date":datetime.now(),
            "time_out":datetime.now().time(),
            "note":"test"
        }
    staff = Staff.objects.get(employee_code=staff_id)
    print(staff)
    attend = attendance(employee_code=staff)
    serializer = attendanceSerializer(attend,data=data_attend)
    # attends = attendance.objects.filter(employee_code=staff_id)
    # print(attends.values())
    if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_200_OK
            )
    else:
            return Response(serializer.errors)
    

