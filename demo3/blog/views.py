from django.shortcuts import render,get_object_or_404,redirect,reverse
from django.views.generic import View
from .models import *  #引入所有模型类
from comments.forms import CommentForm #引入表单
from comments.models import Comment

# Create your views here.

class IndexView(View):
    def get(self,req):
        articles= Article.objects.all() #得到所有文章
        return render(req,"blog/index.html",locals())

class SingleView(View):
    def get(self,req,id):
        article=get_object_or_404(Article,pk=id)
        #向详情页传递一个评论表单
        cf=CommentForm()
        return render(req,"blog/single.html",locals())
    def post(self,req,id):
        name=req.POST.get("name")
        url=req.POST.get("url")
        email=req.POST.get("email")
        content=req.POST.get("content")

        comment=Comment()
        comment.name=name
        comment.url=url
        comment.email=email
        comment.content=content
        comment.article=get_object_or_404(Article,pk=id)
        comment.save()
        return redirect(reverse("blog:single",args=(id,)))





