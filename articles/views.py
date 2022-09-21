from datetime import date
from http.client import HTTPResponse
from unicodedata import name
from django.shortcuts import render
from .models import Art
from .models import image
from django.http import HttpResponse

# Create your views here.
def index(request):
   arts = Art.objects.all()
   # art1 = Art()
   # art1.img = 'image_5.jpg'
   # art1.name = 'lorem'
   # art1.author = 'Lorem'
   # art1.date = '18-09-2022'
   # art1.desc = 'Lorem ipsum, dolor sit amet consectetur adipisicing elit. Explicabo quasi minus ullam ab, molestias quod incidunt animi tempore aperiam reiciendis repellat vel. Perferendis voluptates magni ullam optio vero deserunt perspiciatis!'
   # # return HttpResponse('home')
   
   # art2 = Art()
   # art2.img = 'image_2.jpg'
   # art2.name = 'lorem'
   # art2.author = 'Lorem'
   # art2.date = '18-09-2022'
   # art2.desc = 'Lorem ipsum, dolor sit amet consectetur adipisicing elit. Explicabo quasi minus ullam ab, molestias quod incidunt animi tempore aperiam reiciendis repellat vel. Perferendis voluptates magni ullam optio vero deserunt perspiciatis!'
   
   # art3 = Art()
   # art3.img = 'image_3.jpg'
   # art3.name = 'lorem'
   # art3.author = 'Lorem'
   # art3.date = '18-09-2022'
   # art3.desc = 'Lorem ipsum, dolor sit amet consectetur adipisicing elit. Explicabo quasi minus ullam ab, molestias quod incidunt animi tempore aperiam reiciendis repellat vel. Perferendis voluptates magni ullam optio vero deserunt perspiciatis!'
   
   # arts = [art1, art2, art3]
   return render(request,'index.html',{'arts':arts})

def about(request):
    return render(request,'about.html')

def cycle(request):
    return render(request,'ourservice.html')

def news(request):
    arts = Art.objects.all()
    return render(request,'news.html',{'arts':arts})

def contact(request):
    return render(request,'contact.html')
# def article_list(request):
#     articles = Article.objects.all().order_by('date')
#     return render(request, 'articles/article_list.html', {'articles':articles})

# def article_detail(request, msg):
#     #return HttpResponse(msg)
#     art=Art.objects.get(slug=msg)
#     return render(request, 'article_detail.html', {'article':art})
 