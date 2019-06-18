from django.template import Library
from ..models import Article,Category,Tag,Ads
register = Library()

@register.simple_tag
def my_tag(num=3):
    return Article.objects.all().order_by("-create_time")[:num]

@register.simple_tag
def getarchives():
    return Article.objects.all().dates("create_time","month")

@register.simple_tag
def getcategory():
    return Category.objects.all()


@register.simple_tag
def gettags():
    return Tag.objects.all()


@register.simple_tag
def getads():
    return Ads.objects.all()

