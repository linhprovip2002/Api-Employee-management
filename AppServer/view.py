
from django.http import HttpResponse
import requests
import time
import shutil
from rest_framework.response import Response

def capture(request):
        try:
            url = 'http://192.168.68.171'

            fileName = 'test23.jpg'
        
            
            r = requests.get(f'{url}/capture?_cb={int(round(time.time() * 1000))})', stream = True)
            
            print(r.status_code)
            open(fileName, 'wb').write(r.content)
            return HttpResponse("thanh cong",status=200)
        except:
            return HttpResponse("Lỗi cam",status=400)
    # return HttpResponse("oke")