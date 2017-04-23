from django.contrib import admin
from pagedown.widgets import AdminPagedownWidget
from .models import Post, Category, Tag
from django import forms
# Register your models here.


class PostForm(forms.ModelForm):
    body = forms.CharField(widget=AdminPagedownWidget())

    class Meta:
        model = Post
        fields = '__all__'


class PostAdmin(admin.ModelAdmin):
    form = PostForm
    list_display = ['title', 'create_time', 'modified_time', 'category', 'author']


# 把新增的PostAdmin注册进来
admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)
