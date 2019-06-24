from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Category(models.Model):
    """
    分类表
    """
    title=models.CharField(max_length=20)

    def __str__(self):
        return self.title


class Blog(models.Model):
    """
    博客表
    """
    title = models.CharField(max_length=20)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    body = models.TextField()
    views=models.IntegerField(default=0)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    create_time=models.DateTimeField(auto_now=True)
    pic= models.ImageField(upload_to='p')

    def __str__(self):
        return self.title


class Word(models.Model):
    logo_word=models.CharField(max_length=30)
    secnd_word=models.CharField(max_length=20)
    content=models.TextField()

    def __str__(self):
        return self.logo_word



class Ads(models.Model):
    """
    轮播图
    """
    picture =models.ImageField(upload_to="ad")
    des=models.TextField()
    url=models.CharField(max_length=20)


    def __str__(self):
        return self.des
from tinymce.models import HTMLField

class MessageInfo(models.Model):
    name=models.CharField(max_length=20)
    email = models.EmailField()
    info=HTMLField()

    def __str__(self):
        return self.name


