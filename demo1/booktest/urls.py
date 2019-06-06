from django.conf.urls import url
from.views import index,list,detail,deletebook
app_name='booktest'

#将视图函数加入这
#路由传参
urlpatterns =[

    url(r'^list/$',list,name='list'),
    #通过正则分组 传递参数,通过()传参 视图函数需要添加形参
    url(r'^detail/(\d+)/$',detail,name='detail'),
    url(r'^$',index,name='index'),
#删除书相关
    url(r'^deletebook/(\d+)/$',deletebook,name='deletebook'),
]