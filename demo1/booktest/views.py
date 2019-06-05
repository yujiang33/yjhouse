from django.shortcuts import render
from django.http import HttpResponse
from .models import BookInfo,HereInfo

from django.template import loader
"""
MVT中的V编写视图
"""
# Create your views here.
#写视图函数
# 视图函数由系统调用,系统调用时给req赋值
def index(req):
    # return HttpResponse(f"这里是首页{id}")
    temp =loader.get_template('booktest/index.html')
    res= temp.render({"username":"余江","gender":"男"})
    return HttpResponse(res)


def list(req):
    # return HttpResponse("这里是列表页")

    books = BookInfo.objects.all()

    #用html得到模块.
    temp = loader.get_template('booktest/list.html')
    #将数据库数据渲染     使用末班渲染动态数据
    res = temp.render({'books':books})
    #返回渲染结果
    return HttpResponse(res)

def detail(req,id):
    # return HttpResponse(f"这里是详情第{id}{num}页")
    book = BookInfo.objects.get(pk=id)
    temp = loader.get_template('booktest/detail.html')
    res = temp.render({'book':book})
    return HttpResponse(res)

