from datetime import date
from msilib.schema import LockPermissions
from django.http import HttpResponse
from django.shortcuts import render

# def index(request):
#    art1 = Art()
#    art1.img = 'image_5.jpg'
#    art1.name = 'lorem'
#    art1.author = 'Lorem'
#    art1.date = '18-09-2022'
#    art1.desc = 'Lorem ipsum, dolor sit amet consectetur adipisicing elit. Explicabo quasi minus ullam ab, molestias quod incidunt animi tempore aperiam reiciendis repellat vel. Perferendis voluptates magni ullam optio vero deserunt perspiciatis!'
#    # return HttpResponse('home')
   
#    art2 = Art()
#    art2.img = 'image_2.jpg'
#    art2.name = 'lorem'
#    art2.author = 'Lorem'
#    art2.date = '18-09-2022'
#    art2.desc = 'Lorem ipsum, dolor sit amet consectetur adipisicing elit. Explicabo quasi minus ullam ab, molestias quod incidunt animi tempore aperiam reiciendis repellat vel. Perferendis voluptates magni ullam optio vero deserunt perspiciatis!'
   
#    art3 = Art()
#    art3.img = 'image_3.jpg'
#    art3.name = 'lorem'
#    art3.author = 'Lorem'
#    art3.date = '18-09-2022'
#    art3.desc = 'Lorem ipsum, dolor sit amet consectetur adipisicing elit. Explicabo quasi minus ullam ab, molestias quod incidunt animi tempore aperiam reiciendis repellat vel. Perferendis voluptates magni ullam optio vero deserunt perspiciatis!'
   
#    arts = [art1, art2, art3]
#    return render(request,'index.html',{'arts':arts})

def about(request):
    return HttpResponse('about')