from django.db import models

# Create your models here.
class Question(models.Model):
    title=models.CharField(max_length=30)
    create_time=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title    #让title为  描述title


class Choice(models.Model):
    title=models.CharField(max_length=30)
    question =models.ForeignKey(Question,on_delete=models.CASCADE)
    votes=models.IntegerField(default=0)

    def __str__(self):
        return self.title





