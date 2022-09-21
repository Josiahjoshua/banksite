from asyncio.windows_events import NULL
from email.mime import image
from pyexpat import model
from turtle import title
from unicodedata import name
from django.db import models

# Create your models here.
# class Art:
#     id:int
#     name:str
#     img:str
#     desc:str
#     price:int

class Art(models.Model):
    img = models.ImageField(upload_to='asset/images',null=True,blank=True,height_field=None, width_field=None, max_length=100)
    name = models.CharField(max_length=100)
    # slug = models.SlugField()
    desc = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

# class Article(models.Model):
#     image = models.ImageField(upload_to='',null=True,blank=True,height_field=None, width_field=None, max_length=100)
#     title = models.CharField(max_length=100)
#     slug = models.SlugField()
#     body = models.TextField()
#     date = models.DateTimeField(auto_now_add=True)
#     #add thumbanail and author 


    def __str__(self):
        return self.name

    # def snippet(self):
    #     return self.body[:50] + '...'