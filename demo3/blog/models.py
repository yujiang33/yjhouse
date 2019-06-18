from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Tag(models.Model):
    """
    标签表        与文章多对多
    """
    title = models.CharField(max_length=20,)


    def __str__(self):
        return self.title

class Category(models.Model):
    """
    分类表     与文章一对多
    """
    title = models.CharField(max_length=20,)
    def __str__(self):
        return self.title


class Article(models.Model):
    """
    文章表  与文章多对多, 与标签多对一
    """
    title=models.CharField(max_length=20)
    body=models.TextField()
    category =models.ForeignKey(Category,on_delete=models.CASCADE)
    tag= models.ManyToManyField(Tag,)
    create_time=models.DateTimeField(auto_now=True)
    update_time=models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE)  #使用django自带用户表
    views= models.IntegerField(default=0) #阅读数

    def __str__(self):
        return self.title


class Ads(models.Model):
    """
    轮播图
    """
    pic = models.ImageField(upload_to="ads")
    desc = models.CharField(max_length=30)
    url = models.CharField(max_length=20)

    def __str__(self):
        return self.desc


from tinymce.models import HTMLField

class MessageInfo(models.Model):
    email= models.EmailField()
    # info= models.TextField()
    info=HTMLField()      #TextField 不具备格式,使用富文本替换.此时是Html格式富文本.

    def __str__(self):
        return self.email







