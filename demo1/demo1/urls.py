"""demo1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
"""
项目路由
demo1下方的urls为项目总路由
"""
from django.contrib import admin
from django.urls import path

from django.conf.urls import url,include

urlpatterns = [
    path('admin/', admin.site.urls),
    # 这项目路由下添加 项目应用booktest的路由然后在项目应用下建立路由文件(urls.py)
    #进入应用下新建的urls.py,引入views.py 的视图方法。

    url('booktest/',include('booktest.urls'))
]
