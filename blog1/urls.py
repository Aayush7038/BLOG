from django.urls import path,include
from blog1 import views

app_name='blog1'
urlpatterns=[
    path('',views.blogHome,name='blogHome'),
    #path('<str:slug>',views.blogPost,name='blogPost'),
    path('<int:pk>',views.blogPost,name='blogPost'),
    path('like', views.like_post,name="like_post"),    
]