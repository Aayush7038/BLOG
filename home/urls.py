from django.urls import path
from home import views
from django.views.generic import TemplateView
from home.views import AboutView
from django.views.generic import RedirectView

app_name='home'
urlpatterns=[
    #path("",views.home,name='home'),
    #path("about/",views.about,name='about'),
    path('',TemplateView.as_view(template_name='home/home.html'),name='home'),
    path("about/",AboutView.as_view(),name='about'),
    path("search/",views.search,name='search'),
    
    #path("about/",RedirectView.as_view(url='https://www.amazon.in/'),name='about'),
]