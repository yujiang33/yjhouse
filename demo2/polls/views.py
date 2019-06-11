from django.shortcuts import render,redirect,reverse
from django.views.generic import View
from .models import Question,Choice
# Create your views here.
# locals()是一个字典,可以代替下面的{"questions":questions}


# 装饰器
def checklogin(func):
    def check(self,req,*args):
        if req.session.get('username'):
            return func(self,req,*args)
        else:
            return redirect(reverse("polls:login"))
    return check




class IndexView(View):
    @checklogin
    def get(self,req):
        questions = Question.objects.all()
        return render(req,'polls/index.html',locals())

class DetailView(View):
    @checklogin
    def get(self,req,id):
        question=Question.objects.get(pk=id)
        return render(req,'polls/detail.html',{"question":question})
    @checklogin
    def post(self,req,id):
        c_id =req.POST.get('info')
        choice = Choice.objects.get(pk=c_id)
        choice.votes += 1
        choice.save()
        return redirect(reverse("polls:result",args=(id,)))

class ResultView(View):
    @checklogin
    def get(self,req,id):
        question=Question.objects.get(pk=id)
        return render(req,"polls/result.html",{"question":question})

class LoginView(View):

    def get(self,req):
        return render(req,'polls/login.html')
    def post(self,req):
        username =req.POST.get('username')
        pwd= req.POST.get('password')
        req.session['username']=username
        return redirect(reverse("polls:index"))







