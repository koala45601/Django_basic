from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime, time


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




