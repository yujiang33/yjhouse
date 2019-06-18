from django.shortcuts import render,redirect,reverse   #redirect,reverse是简写HttpResponseRedirect
from django.http import HttpResponse
# from django.http import HttpResponseRedirect
from .models import BookInfo,HereInfo
from django.template import loader
"""
MVT中的V编写视图
"""
# Create your views here.
#写视图函数
# 视图函数由系统调用,系统调用时给req赋值
def index(req):
    #简写模板。。
    return render(req,'booktest/index.html',{'username':'余江'},{"gender":"男"})


def list(req):
    books = BookInfo.objects.all()
    return render(req,'booktest/list.html',{'books':books})

def detail(req,id):
    book = BookInfo.objects.get(pk=id)
    return render(req,'booktest/detail.html',{'book',book})
                  #请求， 模板名下/的要跳转的页面html，字典{}

#删除英雄
def deletehero(req,id):
    hero= HereInfo.objects.get(pk=id)
    hero.delete()
   #重定向删除完消失删除的角色，还在详情页。
    return redirect(reverse('booktest:detail',args=(hero.book.id,)))
#删除书方法
def deletebook(req,id):
    b= BookInfo.objects.get(pk=id)
    b.delete()
    return redirect(reverse('booktest:list'))
#添加角色
def addhero(req,id):
    book = BookInfo.objects.get(pk=id)
    if req.method =='GET':
        return render(req,"booktest/addhero.html",{'book':book})
    elif req.method =='POST':
        hero = HereInfo()
        hero.name =req.POST.get('heroname')
        hero.gender=req.POST.get('sex')
        hero.content=req.POST.get('herocontent')
        hero.book=book
        hero.save()
        return redirect(reverse('booktest:detail',args=(id,)))

#添加书籍
def addbook(req):
    if req.method == 'GET':
        return render(req,'booktest/addbook.html')
    elif req.method == 'POST':
        book = BookInfo()
        book.title=req.POST.get('title')
        book.pub_date=req.POST.get('pub_date')
        book.save()
        return redirect(reverse('booktest:list'))

# 书籍添加成功后，return 要在list 上显示出来添加的书籍。所以
# return redirect(reverse("booktest:list"))
# 如果有参数，后面args=(id,)
# return redirect(reverse("booktest:list"，args=(id,))
#redirect reverse            视图函数名list






