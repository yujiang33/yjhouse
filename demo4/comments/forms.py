from django import forms
from .models import Comment

#使用表单生成页面,根据评论模型生成表单
class CommentForm(forms.ModelForm):
    class Meta():
        model=Comment
        fields=['name','content','email','url']


        #重定义字段模型类的content字段属性.之前写错属性
        widget={
            'content':forms.Textarea()
        }