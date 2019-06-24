from django.shortcuts import render,HttpResponse,get_object_or_404,redirect,reverse
from django.views.generic import View
from .models import *
from comments.forms import CommentForm
from comments.models import Comment
import markdown  #让编写文章有了http格式,但是需要markdown写法代码和内容
from django.core.paginator import Paginator

# Create your views here.


class IndexView(View):
    def get(self,req):
        words=Word.objects.all()

        return render(req,'sport/index.html',{"words":words})

class BlogView(View):
    def get(self,req):
        blogs=Blog.objects.all() # 得到所有博客

        paginator=Paginator(blogs,3)
        pagenum=req.GET.get('page')
        pagenum=1 if pagenum==None else pagenum
        page=paginator.get_page(pagenum)
        page.path=reverse('sport:blog')  #点击页面要跳转到这个blog页面
        return render(req,'sport/blog.html',{'page':page})    # {'page':page}字典

class SingleView(View):
    def get(self,req,id):
        blog=get_object_or_404(Blog,pk=id)
        # 1.对指定的字段使用markdown渲染成html格式
        md = markdown.Markdown(extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
            'markdown.extensions.toc'
        ])
        # 2. 使用markdown实例渲染指定字段
        blog.body = md.convert(blog.body)
        # 3.将md的目录对象赋予 article
        blog.toc = md.toc
        # 4.进入admin管理员,修改文章为markdown格式,在指定地方使用[TOC]插入目录,然后使用转义
        # {{blog.body|safe}}    {{blog.toc|safe}}  |safe转义
        cf=CommentForm()
        return render(req,'sport/single.html',locals())         #local() 字典,,,返回所有字典.相比较,性能差.

    def post(self,req,id):
        name=req.POST.get('name')
        url=req.POST.get('url')
        email=req.POST.get('email')
        content=req.POST.get('content')

        comment=Comment()
        comment.name=name
        comment.url=url
        comment.email=email
        comment.content=content
        comment.blog=get_object_or_404(Blog,pk=id)
        comment.save()
        return redirect(reverse('sport:single',args=(id,)))

class CategoryView(View):
    def get(self,req,id):
        category=get_object_or_404(Category,pk=id)
        blogs= category.blog_set.all()
# 分页
        paginator = Paginator(blogs, 3)
        pagenum = req.GET.get('page')
        pagenum = 1 if pagenum == None else pagenum
        page = paginator.get_page(pagenum)
        page.path = "/category/%s/"%(id,)
        return render(req,"sport/blog.html",{'page':page})

class ArchievesView(View):
    def get(self,req,year,month):
        blogs =Blog.objects.filter(create_time__year=year,create_time__month=month)

        paginator = Paginator(blogs, 3)
        pagenum = req.GET.get('page')
        pagenum = 1 if pagenum == None else pagenum
        page = paginator.get_page(pagenum)
        page.path="/archieves/%s/%s/"%(year,month)
        return render(req,"sport/blog.html",{'page':page})


class ContactView(View):
    def get(self,req):
        return render(req,'sport/contact.html')
    def post(self,req):
        name=req.POST.get('name')
        email=req.POST.get('email')
        message=req.POST.get('message')

        info=MessageInfo()
        info.name=name
        info.email=email
        info.info=message
        info.save()
        return HttpResponse('建议已成功')