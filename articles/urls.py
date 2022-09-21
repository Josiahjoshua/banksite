from django.urls import path
from .import views

app_name='articles'

urlpatterns = [
    path('',views.index),
    path('index.html',views.index),
    path('about.html', views.about),
    path('ourservice.html', views.cycle),
    path('news.html', views.news),
    path('contact.html', views.contact)
    # path('<slug:msg>',views.article_detail, name='detail'),
]
