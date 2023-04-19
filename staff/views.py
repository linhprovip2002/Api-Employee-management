from datetime import datetime
from staff.models import Staff, attendance
from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.http import HttpResponse
from rest_framework.response import Response
from staff.api.serializers import StaffSerializer, attendanceSerializer, statisticalAttend
from auth_app.models import Person
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
import json


@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def create(request):
    print(request.user)
    person = Person.objects.get(username=request.user)
    staff = Staff(id=request.user)
    data = {
        'employee_code': request.data.get('employee_code'),
        'first_name': request.data.get('first_name'),
        'last_name': request.data.get('last_name'),
        'phone': request.data.get('phone'),
        'department': request.data.get('department'),
        'age': request.data.get('age'),
        'img': request.data.get('img'),
        'position': request.data.get('position'),
        'id': person.id
    }
    serializer = StaffSerializer(staff, data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
def detail_user_login(request):
    # print("id:" + str(request.user.id))
    # staff = Staff.objects.filter(id=request.user.id)
    try:
        staff = Staff.objects.get(id=request.user)
        serializer = StaffSerializer(staff)
        return Response(serializer.data)
    except Staff.DoesNotExist:
        return Response("staff not found", status=status.HTTP_404_NOT_FOUND)


@ api_view(['GET'])
@ authentication_classes([TokenAuthentication])
def get_detail_staff(request, staff_id):
    print(request.user)
    staff = Staff.objects.get(employee_code=staff_id)
    if (staff == None):
        return Response("staff not found", status=status.HTTP_404_NOT_FOUND)
    serializer = StaffSerializer(staff)
    return Response(serializer.data)


@ api_view(['GET'])
@ authentication_classes([TokenAuthentication])
def get_detail_staff_by_id(request, id):
    staff = Staff.objects.get(id=id)
    print(staff)
    if staff:
        serializer = StaffSerializer(staff)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response("staff not found", status=status.HTTP_404_NOT_FOUND)


@ api_view(['GET'])
@ authentication_classes([TokenAuthentication])
def get_all_staff(request):
    params = request.GET
    print(params)
    staff = Staff.objects.all()
    if (staff == None):
        return Response("staff not found", status=status.HTTP_404_NOT_FOUND)
    serializer = StaffSerializer(staff, many=True)
    return Response(serializer.data)


@ api_view(['PUT'])
@ authentication_classes([TokenAuthentication])
@ permission_classes([IsAuthenticated])
def update_staff(request, staff_id):
    try:
        staff = Staff.objects.get(employee_code=staff_id)
        print(staff.id_id)
        person = Person.objects.get(username=request.user)
        if person.is_admin == False:
            return Response("you not have admin permission", status=status.HTTP_401_UNAUTHORIZED)
        else:
            data = {
                'employee_code': request.data.get('employee_code'),
                'first_name': request.data.get('first_name'),
                'last_name': request.data.get('last_name'),
                'phone': request.data.get('phone'),
                'department': request.data.get('department'),
                'age': request.data.get('age'),
                'img': request.data.get('img'),
                'position': request.data.get('position'),
                'id': staff.id_id
            }
            serializer = StaffSerializer(staff, data=request.data)
            serializer = StaffSerializer(staff, data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except:
        return Response("staff not found", status=status.HTTP_404_NOT_FOUND)


@ api_view(['DELETE'])
@ authentication_classes([TokenAuthentication])
@ permission_classes([IsAuthenticated])
def delete_staff(request, staff_id):
    try:
        staff = Staff.objects.get(employee_code=staff_id)

        person = Person.objects.get(username=request.user)
        if person.is_admin == False:
            return Response("you not have admin permission", status=status.HTTP_401_UNAUTHORIZED)
        else:
            staff.delete()
            return Response("delete success", status=status.HTTP_200_OK)
    except:
        return Response("staff not found", status=status.HTTP_404_NOT_FOUND)
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


def get_user_in_day(staff_id):
    day = datetime.now().day
    attends = attendance.objects.filter(
        employee_code=staff_id, date__day=day, date__month=datetime.now().month, date__year=datetime.now().year)
    print(attends.values())
    if attends:
        return True
    else:
        return False


@ api_view(['GET'])
def get_attendance_by_day(request):
    params = request.GET
    day = params.get('day')
    month = params.get('month')
    year = params.get('year')
    if day:
        attends = attendance.objects.filter(date__day=int(
            day), date__month=int(month), date__year=int(year))
        if attends:
            serializer = statisticalAttend(attends, many=True)
            return Response(serializer.data)
        else:
            return Response("no data", status=204)
    else:
        print("doo day roi")
        attends = attendance.objects.filter(
            date__month=int(month), date__year=int(year))
        if attends:
            serializer = statisticalAttend(attends, many=True)
            return Response(serializer.data)
        else:
            return Response("no data", status=204)


@ api_view(['POST'])
def create_time_in(request, staff_id):
    data_attend = {
        "date": datetime.now().date(),
        "time_in": datetime.now().time(),
        "note": "test"
    }
    print(get_user_in_day(staff_id))
    if get_user_in_day(staff_id):
        return Response("This person has taken attendance,Do you want log out?")
    else:
        staff = Staff.objects.get(employee_code=staff_id)
        print(staff.img)
        attend = attendance(employee_code=staff)
        # value_attend = attendance.objects.filter(date = datetime.now().date())

        serializer = attendanceSerializer(attend, data=data_attend)

        data = {
            "employee_code": staff_id,
            "first_name": staff.first_name,
            "last_name": staff.last_name,
            "img":"/media/" + str(staff.img),
            "position": staff.position,
            "department": staff.department,
        }
        if serializer.is_valid():
            serializer.save()
            return Response(
                {**serializer.data, **data},
                status=status.HTTP_200_OK
            )
        else:
            return Response(serializer.errors, status=400)


@ api_view(['PUT'])
def update_time_out(request, staff_id):
    day = datetime.now().day
    month = datetime.now().month
    year = datetime.now().year
    try:
        staff = Staff.objects.get(employee_code=staff_id)
        attendance_record = attendance.objects.get(
        employee_code=staff_id, date__day=day, date__month=month, date__year=year)
        data_attend = {
            "time_in": attendance_record.time_in,
            "time_out": datetime.now().time(),
            "date": attendance_record.date,
            "note": attendance_record.note
        }
        serializer = attendanceSerializer(attendance_record, data=data_attend)
        data_staff = {
            "employee_code": staff_id,
            "first_name": staff.first_name,
            "last_name": staff.last_name,
            "img": str(staff.img),
            "position": staff.position,
            "department": staff.department,
        }
        if serializer.is_valid():
            serializer.save()
            return Response({**serializer.data, **data_staff}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors)
    except Staff.DoesNotExist:
        return Response({"error": f"Staff with employee code {staff_id} does not exist."}, status=status.HTTP_404_NOT_FOUND)
    except attendance.DoesNotExist:
        return Response({"error": f"Attendance record for staff with employee code {staff_id} does not exist."}, status=status.HTTP_404_NOT_FOUND)


@ api_view(['DELETE'])
@ permission_classes([IsAuthenticated])
def delete_attend(request, staff_id):
    print(request.user)
    print(staff_id)
    person = Person.objects.get(username=request.user)
    if person.is_admin == False:
        return Response("you not have admin permission")
    else:
        attend = attendance.objects.filter(employee_code=staff_id)
        attend.delete()
        return Response("delete success")


@ api_view(['GET'])
# @permission_classes([IsAuthenticated])
def get_attend(request, staff_id):

    attend = attendance.objects.filter(employee_code=staff_id)
    date = [attend.date.strftime('%d') for attend in attend]
    if date:
        return Response(date)
    else:
        return Response("no data")
# get user check in  day in month


@ api_view(['GET'])
def get_attend_statistical(request, staff_id):
    params = request.GET
    month = params.get('month')
    year = params.get('year')
    if month:
        attends = attendance.objects.filter(
            employee_code=staff_id, date__month=int(month), date__year=int(year))
        if attends:
            serializer = statisticalAttend(attends, many=True)
            return Response(serializer.data)
        else:
            return Response("no data", status=204)
    else:
        attends = attendance.objects.filter(
            employee_code=staff_id, date__year=int(year))
        if attends:
            serializer = statisticalAttend(attends, many=True)
            return Response(serializer.data)
        else:
            return Response("no data", status=204)
# @api_view(['GET'])
# def get_attend_by_month(request):
#     params = request.GET
#     month = params.get('month')
#     attends = attendance.objects.all()
#     date = [attend.date.strftime('%m') for attend in attends]
#     print(date)
#     print(month)
#     return Response("oke")
from django.db.models import Count
@api_view(['GET'])
def get_attend_statistical_by_month(request):
    params = request.GET
    month = params.get('month')
    year = params.get('year')

   
    if month and year:
       
        month = int(month)
        year = int(year)

       
        attends = attendance.objects.filter(date__month=month, date__year=year).values('employee_code')

        total_days_in_month = datetime(year, month + 1, 1).toordinal() - datetime(year, month, 1).toordinal()

   
        result = attends.annotate(total_days=Count('date')).values('employee_code', 'total_days')

        staff_data = Staff.objects.filter(employee_code__in=[attend['employee_code'] for attend in result]).values('first_name', 'last_name', 'img')

        response_data = []
        for attend in result:
            staff = staff_data.get(employee_code=attend['employee_code'])
            response_data.append({
                'first_name': staff['first_name'],
                'last_name': staff['last_name'],
                'img': "/media/"+staff['img'],
                'total_days': attend['total_days']
            })

        return Response(response_data)
    else:
        return Response("no params", status=204)

