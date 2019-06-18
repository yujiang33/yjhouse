from django.shortcuts import render,redirect,reverse
from django.views.generic import View
from .models import Question,Choice,MyUser
from .forms import MyUserLoginForm,MyUserRegistForm
from django.contrib.auth import authenticate,login,logout
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
        return render(req,"polls/result.html",{"question":question}) #显示内容在当前页面

class LoginView(View):
    def get(self,req):
        lf = MyUserLoginForm()
        rf = MyUserRegistForm()
        return render(req,"polls/login_regist.html", locals())

    def post(self,req):
        username = req.POST.get("username")
        password = req.POST.get("password")

        # MyUser.objects.get(username = username,password = password)
        # 使用django自带授权系统  如果授权成功返回user
        user = authenticate(req, username = username, password = password)
        if user:
            # 在客户端存储cookie
            login(req,user)
            return redirect(reverse("polls:index"))
        else:
            lf = MyUserLoginForm()
            rf = MyUserRegistForm()
            errormessage = "登录失败"
            return render(req, "polls/login_regist.html", locals())



class RegistView(View):
    def get(self,req):
        pass
    def post(self,req):
        # rf = MyUserRegistForm(req.POST)
        # rf.save()

        try:
            username = req.POST.get("username")
            password = req.POST.get("password")
            email = req.POST.get("email")

            user =MyUser.objects.create_user(username=username, email=email, password=password)
            if user:
                return redirect(reverse("polls:login"))

        except:
            lf = MyUserLoginForm()
            rf = MyUserRegistForm()
            errormessage ="注册失败"
            return render(req, "polls/login_regist.html", locals())


class LogOutView(View):
    def get(self,req):
        logout(req)
        return redirect(reverse("polls:login"))







