from django import forms
from .models import Comment
#使用表单生成页面
#根据评论模型类生成表单类
class CommentForm(forms.ModelForm):
    class Meta():
        model = Comment
        fields=["name","content","email","url"]
        # 重定义字段
        widgets={
            "content":forms.Textarea()
        }