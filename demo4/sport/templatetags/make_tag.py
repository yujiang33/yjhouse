# 自定义标签
from django.template import Library
from ..models import Ads,Blog,Category
from comments.models import Comment
register=Library()

@register.simple_tag
def getads():
    return Ads.objects.all()

@register.simple_tag
def getcategory():
    return Category.objects.all()

@register.simple_tag
def getarchieves():
    return Blog.objects.all().dates("create_time","month")

@register.simple_tag
def getnews(num=4):
    return Blog.objects.all().order_by("-create_time")[:num]

