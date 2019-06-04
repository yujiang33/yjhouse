from django.db import models
"""
MVT里面的M
"""
# Create your models here.
# 继承models.Model就有了父类ORM的功能
class BookInfo(models.Model):
    title =models.CharField(max_length=20)
    pub_date = models.DateTimeField()

class HereInfo(models.Model):
    name = models.CharField(max_length=20)
    gender = models.BooleanField(default=True)
    content = models.CharField(max_length=100)
    book = models.ForeignKey(BookInfo,on_delete=models.CASCADE)
    # book作为外键关联到bookinfo表