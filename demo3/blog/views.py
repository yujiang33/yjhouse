from django.shortcuts import render,get_object_or_404,redirect,reverse,HttpResponse
from django.views.generic import View
from .models import *  #引入所有模型类
from comments.forms import CommentForm #引入表单
from comments.models import Comment
from django.core.paginator import Paginator
import markdown  #引入markdown
from django.core.mail import send_mail,EmailMultiAlternatives
from django.views.decorators.cache import cache_page  #引入缓存装饰器
# Create your views here.


class IndexView(View):
    def get(self,req):
        articles= Article.objects.all() #得到所有文章

        paginator = Paginator(articles, 2)
        pagenum = req.GET.get('page')
        pagenum = 1 if pagenum == None else pagenum
        page = paginator.get_page(pagenum)
        page.path = "/"
        return render(req,"blog/index.html",{'page':page})   #传{'page':page}        local(),包括所有局部变量所以,影响性能

@cache_page(30)
def index(req):
    articles = Article.objects.all()
    paginator = Paginator(articles, 2)
    pagenum = req.GET.get('page')
    pagenum = 1 if pagenum == None else pagenum
    page = paginator.get_page(pagenum)
    page.path = "/"
    return render(req, "blog/index.html", {'page': page})




class SingleView(View):
    def get(self,req,id):
        article=get_object_or_404(Article,pk=id)
        #1.对指定的字段使用markdown渲染成html格式
        md = markdown.Markdown(extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
            'markdown.extensions.toc'
        ])
        #2. 使用markdown实例渲染指定字段
        article.body =md.convert(article.body)
        #3.将md的目录对象赋予 article
        article.toc=md.toc
        #4.进入admin管理员,修改文章为markdown格式,在指定地方使用[TOC]插入目录,然后使用转义
        #{{article.body|safe}}    {{article.toc|safe}}  |safe转义
        #

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


class ArchivesView(View):
    def get(self,req,year,month):
        articles=Article.objects.filter(create_time__year=year,create_time__month= month)

        paginator = Paginator(articles,2)
        pagenum=req.GET.get('page')
        pagenum= 1 if pagenum==None else pagenum
        page = paginator.get_page(pagenum)
        page.path="/archives/%s/%s/"%(year,month)
        return render(req,"blog/index.html",{'page':page})

class CategoryView(View):
    def get(self,req,id):
        category =get_object_or_404(Category,pk=id)
        #通过分类找到分类里的所有文章
        articles =category.article_set.all()

        paginator = Paginator(articles, 2)
        pagenum = req.GET.get('page')
        pagenum = 1 if pagenum == None else pagenum
        page = paginator.get_page(pagenum)
        page.path = "/category/%s/"%(id,)
        return render(req, "blog/index.html", {'page':page})

class TagsView(View):
    def get(self,req,id):
        tags=get_object_or_404(Tag,pk=id)
        articles=tags.article_set.all()

        paginator = Paginator(articles, 2)
        pagenum = req.GET.get('page')
        pagenum = 1 if pagenum == None else pagenum
        page = paginator.get_page(pagenum)
        page.path = "/tags/%s/"%(id,)
        return render(req,"blog/index.html",{'page':page})

class ContactView(View):
    def get(self,req):
        return render(req,'blog/contact.html')

    def post(self,req):
        email =req.POST.get('email')
        message=req.POST.get('message')

        info=MessageInfo()
        info.email=email
        info.info=message
        info.save()
        return HttpResponse('建议成功')



class SendMailView(View):
    def get(self,req):
        try:
            mail=EmailMultiAlternatives(subject="测试邮件HTML格式", body="<h1>  <a href = 'http://www.baidu.com'> 百度 </a>  </h1> ", from_email= settings.DEFAULT_FROM_EMAIL,to= ["18137128152@163.com", "zhangzhaoyu@qikux.com"] )
            mail.content_subtype='html'
            mail.send()
            return HttpResponse('发送成功')
        except:
            return HttpResponse('发送失败')













