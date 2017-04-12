from django.db import models
from django.contrib.auth.models import User
from django.utils.six import python_2_unicode_compatible
from django.urls import reverse
# Create your models here.


# 文章分类
@python_2_unicode_compatible
class Category(models.Model):
    name = models.CharField(max_length=100)

    # 装饰器为了兼容python2
    def __str__(self):
        return self.name


# 文章标签
@python_2_unicode_compatible
class Tag(models.Model):
    name = models.CharField(max_length=100)

    # 装饰器为了兼容python2
    def __str__(self):
        return self.name


# 文章
@python_2_unicode_compatible
class Post(models.Model):
    # 文章标题
    title = models.CharField(max_length=80)
    # 文章内容
    body = models.TextField()
    # 存储文章创建时间和最后更新时间
    create_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    # 文章摘要，可以为空
    excerpt = models.CharField(max_length=100, blank=True)

    # 分类与标签，使用外键,一篇文章可以对应多个标签，一个标签也可以
    # 对应多篇文章，使用ManyToManyField
    category = models.ForeignKey(Category)
    tags = models.ManyToManyField(Tag, blank=True)

    # 文章作者
    author = models.ForeignKey(User)

    def __str__(self):
        return self.title

    # blog:detail表示blog应用下的name=detail函数
    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})
