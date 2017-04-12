from django.db import models
from django.contrib.auth.models import User
# Create your models here.

#文章分类 
class Category(models.Model):
    name = models.CharField(max_length=100)


#文章标签
class Tag(models.Model):
    name = models.CharField(max_length=100)

#文章
class Post(models.Model):
    #文章标题
    title = models.CharField(max_length=80)
    #文章内容
    body = models.TextField()
    #存储文章创建时间和最后更新时间
    create_time = models.DateTimeField()
    modified_time = models.DateTimeField()

    #文章摘要，可以为空
    excerpt = models.CharField(max_length=100, blank=True)

    #分类与标签，使用外键,一篇文章可以对应多个标签，一个标签也可以
    #对应多篇文章，使用ManyToManyField
    category = models.ForeignKey(Category)
    tags = models.ManyToManyField(Tag, blank=True)

    #文章作者
    author = models.ForeignKey(User)

