from django.urls import path
from . import views
from video.views import ArticleDetail, categories,categoryviews

app_name='video'
urlpatterns=[
    path('postComment',views.postComment,name="postComment"),
    #path('category/',views.categorylist,name='categorylist'),
    path('category/',categories.as_view(),name='categorylist'),
    #path('<slug:category_slug>/',views.categoryview,name='categoryview'),
    path('<slug:category_slug>/',categoryviews.as_view(),name='categoryview'),
    path('<slug:article_slug>',views.articledetail,name='articledetail'),
    #path('<slug:article_slug>',ArticleDetail.as_view(),name='articledetail'),
    ]

