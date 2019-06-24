from django.db import models
from sport.models import Blog
# Create your models here.

class Comment(models.Model):
    """
    评论表,与博客多对一关系
    """
    name= models.CharField(max_length=20,verbose_name='姓名')
    create_time=models.DateTimeField(auto_now=True)
    content=models.TextField(max_length=500,verbose_name='正文')
    email=models.EmailField(blank=True,null=True,verbose_name='邮箱')
    url=models.URLField(blank=True,null=True,verbose_name="个人主页")
    blog=models.ForeignKey(Blog,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
