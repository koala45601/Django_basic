from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime, time

'''def [hello_hompage] = มีไว้สำหรับ เป็นต้องส่งค่า request ไปยัง urls.py หรือก็คือ  hello_hompage คือชื่อตัวเว็บที่ส่งค่าไปเช่น ip web คือ 127.0.0.1:8000 
แล้วถ้าอยากได้ข้อความหรือค่าที่ มีอยุ่ใน def ให้ใช้ 127.0.0.1:8000/hello_homepage แต่ต้องไปเพิ่มใน urls.py ด้วย 

การส่งค่าจะใช้ คำสั่ง return HttpResponse เพื่อส่งค่า
'''
time1=datetime(2021, 2, 2)
print(time1)

def hello_homepage(request):
    return HttpResponse('<h1>HELLO Petong<h1>'+str(time1))

def hello(request, id):
    return HttpResponse('HELLO WORLD ID = '+id )

#การส่งค่าไปที่ index.html
def index(request):
    id3 = '002'
    name = 'somchai'
    email = 'koala4561@gmail.com'
    
    #ประกาศตัวแปรอารเรย์
    act = [
        'Petong',
        'Pow',
        'Tar'

    ]

    #ดิกชินารี เวลาประกาศอะไรให้เอาตัวแปรมาใส่ในนี้ด้วย 
    return render(request, 'index.html',{
        'id2': id3,
        'name2': name,
        'email2' : email,
        'act1': act
    })




def re_path(request):
    return HttpResponse('TEST Aricht')

def re_path_2(request, year):
    return HttpResponse("TEST YEAR : "+str(year))

def re_path_3(request, ID_2, slug):
    return HttpResponse("TEST - in word : "+str(ID_2)+' slug = '+slug)




