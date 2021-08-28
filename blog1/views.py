from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from django.urls.base import reverse
from blog1.models import Post
from django.contrib import messages
from django.template.loader import render_to_string
from django.http import JsonResponse



def blogHome(request):
        print("bloghome")
        allPosts=Post.objects.all()
        context={'allPosts':allPosts}
        return render(request,'blog1/blogHome.html',context)

def blogPost(request,pk):
        post=get_object_or_404(Post,pk=pk)
        is_liked=False
        context={'post':post,'is liked':is_liked,'total_likes':post.total_likes}
        return render(request,'blog1/blogPost.html',context)     


def like_post(request):
        post=get_object_or_404(Post, id=request.POST.get('id'))
        is_liked=False
        if post.likes.filter(id=request.user.id).exists():
                post.likes.remove(request.user)
                is_liked=False
        else:
                post.likes.add(request.user)
                is_liked=True

        context={
                'post' : post,
                'is_liked' : is_liked,
                'total_likes' : post.total_likes
        }

        if request.is_ajax():
                html=render_to_string('blog1/like-section.html',context,request=request)
                return JsonResponse({'from':html})

    
