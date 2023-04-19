from staff import views
from django.urls import path


app_name = 'staff'
urlpatterns = [

    path('create', views.create, name='create'),
    path('detail/<str:staff_id>', views.get_detail_staff, name='detail'),
    path('detail/', views.detail_user_login, name='detail_user_login'),
    path('detail/user/<int:id>', views.get_detail_staff_by_id, name='detail'),
    path('list', views.get_all_staff, name='all'),
    path('detail/<str:staff_id>/update', views.update_staff, name='update'),

    path('detail/<str:staff_id>/delete', views.delete_staff, name='delete'),

    # path('create/', views.StaffViewSet.as_view({'post':'create'}), name='create'),
    # path('list/', views.StaffViewSet.as_view({'get': 'list'}), name='read_all'),
    # path('<str:staff_id>/', views.StaffDetailView.as_view(), name='read_one'),
    path('attendance/statisticalbymonth',
         views.get_attend_statistical_by_month,name="statistical_by_month"),
    path('attendance/statistical',
         views.get_attendance_by_day, name='all_attendance'),
    path('attendance/<str:staff_id>', views.get_attend, name='attendance'),
    path('attendance/<str:staff_id>/create',
         views.create_time_in, name='create_attendance'),
    path('attendance/<str:staff_id>/update',
         views.update_time_out, name='update_attendance'),
    path('attendance/<str:staff_id>/delete',
         views.delete_attend, name='delete_attendance'),
    path('attendance/<str:staff_id>/statistical',
         views.get_attend_statistical, name='detail_attendance'), 
    
]
