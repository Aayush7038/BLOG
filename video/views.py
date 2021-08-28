from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from video.models import CategoryList,Item, VideoComment
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib import messages
from django.urls import reverse

# Create your views here.

#def categorylist(request):
 #   categories=CategoryList.objects.all()
  #  print("called 123")
   # return render(request,'video/categorylist.html',{'categories' : categories})

class categories(ListView):
    model=CategoryList
    context_object_name='categories'
    template_name='video/categorylist.html'


class categoryviews(ListView):
    context_object_name='article'
    template_name='video/categoryview.html'

    def get_queryset(self):
        self.category=get_object_or_404(CategoryList,slug=self.kwargs['category_slug'])
        return Item.objects.filter(category=self.category)

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['categoryview']=self.category
        return context    


#def categoryview(request,category_slug):
#    categoryview=CategoryList.objects.filter(slug=category_slug).first()
#    article=Item.objects.filter(category=categoryview)
#    context={'categoryview':categoryview,'article':article}
#    print("called")
#    return render(request,'video/categoryview.html',context)




def articledetail(request,article_slug):
    article=Item.objects.filter(slug=article_slug).first()
    comments=VideoComment.objects.filter(article=article,parent=None)
    replies=VideoComment.objects.filter(article=article).exclude(parent=None)
    repDict={}
    for reply in replies:
        if reply.parent.srno not in repDict.keys():
            repDict[reply.parent.srno]=[reply]
        else:
            repDict[reply.parent.srno].append(reply)

    context={'article':article,'comments':comments,'user':request.user,'repDict':repDict}
    print("Now I am called")
    return render(request,'video/articledetail.html',context)


    #return render(request,'video/articledetail.html',{'article':article})


class ArticleDetail(DetailView):
    slug_url_kwarg='article_slug'
    model=Item
    template_name='video/articledetail.html'
    context_object_name='article'

def postComment(request):
        if request.method=="POST":
            comment=request.POST.get("comment")
            user=request.user
            articleSno=request.POST.get("articleSno")
            article=Item.objects.get(sno=articleSno)
            parentSno=request.POST.get("parentSno")
            if parentSno=="":
                comment=VideoComment(comment=comment,user=user,article=article)
                comment.save()
                messages.success(request,"Your message has been posted successfully")
                print("if command")
            else:
                parent=VideoComment.objects.get(srno=parentSno)
                comment=VideoComment(comment=comment,user=user,article=article,parent=parent)


                comment.save()
                messages.success(request,"Your reply has been posted successfully")
        print("before return")
        return HttpResponseRedirect(reverse('video:articledetail',args=(article.slug,)))
        