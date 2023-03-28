from staff import views
from django.urls import path


app_name = 'staff'
urlpatterns = [

    path('create',views.create,name='create'),
    path('detail/<str:staff_id>',views.get_detail_staff,name='detail'),
    path('list',views.get_all_staff,name='all'),
    path('detail/<str:staff_id>/update',views.update_staff,name='update'),

   
    # path('create/', views.StaffViewSet.as_view({'post':'create'}), name='create'),
    # path('list/', views.StaffViewSet.as_view({'get': 'list'}), name='read_all'),
    # path('<str:staff_id>/', views.StaffDetailView.as_view(), name='read_one'),


    path('attendance/<str:staff_id>/create',views.create_time_in,name='create_attendance'),

    




    
]