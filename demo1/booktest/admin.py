"""
Django强大的后台管理
应用的admin.pyz注册模型类
"""
from django.contrib import admin
from.models import BookInfo,HereInfo

# Register your models here.
# admin.site.register(BookInfo)
# admin.site.register(HereInfo)

class HereInfoInlines(admin.StackedInline):
    model =HereInfo
    extra =1
class BookInfoAdmin(admin.ModelAdmin):
    # 重写list_display 重写后台显示那些字段
    list_display =('title','pub_date')
    list_filter =('title','pub_date')
    list_per_page =20
    inlines = [HereInfoInlines]
# 在注册模型时，注册该模型的后台管理类 通过管理类重写后台
admin.site.register(BookInfo,BookInfoAdmin)

class HereInfoAdmin(admin.ModelAdmin):
    list_display =('name','content')
    list_filter =('name',) #元组加，
    search_fields =('name','content')
admin.site.register(HereInfo,HereInfoAdmin)




