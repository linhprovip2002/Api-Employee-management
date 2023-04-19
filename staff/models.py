from django.db import models
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from auth_app.models import Person
# Create your models here.

class MyUserManager(BaseUserManager):
  def create_user(self, employee_code, first_name, last_name, number_phone,department,age,img, id,address):
    user = self.model(
      employee_code = employee_code,
      first_name = first_name,
      last_name = last_name,
      number_phone = number_phone,
      address = address,
      department = department,
      age = age,
      img = img,
      id = id,
    )
    user.save(using=self._db)
    return user

class Staff(AbstractBaseUser):
    employee_code = models.CharField(max_length=100, unique=True,primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.IntegerField()
    department = models.CharField(max_length=50)
    age = models.IntegerField()
    img = models.ImageField(upload_to='images/', null=True, blank=True)
    position = models.CharField(max_length=100)
    id = models.ForeignKey(Person, on_delete=models.CASCADE, related_name="staff")
    objects = MyUserManager()    
    
    def __str__(self):
        return self.employee_code
class my_attend(BaseUserManager):
  def create_attend(self, id_attendance, employee_code, date, time_in, time_out, note):
    attend = self.model(
      id_attendance = id_attendance,
      employee_code = employee_code,
      date = date,
      time_in = time_in,
      time_out = time_out,
      note = note,
    )
    attend.save(using=self._db)
    return attend
    

class attendance(AbstractBaseUser):
  id_attendance = models.AutoField(primary_key=True)
  employee_code = models.ForeignKey(Staff, on_delete=models.CASCADE, related_name="attendance")
  date = models.DateField()
  time_in = models.TimeField()
  time_out = models.TimeField(null=True, blank=True)
  note = models.CharField(max_length=10)
  objects = my_attend()
  def __str__(self):
    return self.employee_code

