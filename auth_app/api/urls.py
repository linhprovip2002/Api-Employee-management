from auth_app import views
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
app_name = 'auth_app'
urlpatterns = [
    path('register/', views.register, name='register'),
    # path('login/', obtain_auth_token, name='login'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('detail/', views.detail, name='detail'),
    path('all/', views.all, name='all'),
    path('<int:staff_id>/delete',views.detete,name='delete'),
]