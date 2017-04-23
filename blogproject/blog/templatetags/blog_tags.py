from django import template
from ..models import Post, Category, Tag

register = template.Library()


# 获取数据库中最新的num篇文章
@register.simple_tag
def get_recent_posts(num=5):
    return Post.objects.all().order_by("-create_time")[:num]


@register.simple_tag
def archives():
    return Post.objects.dates('create_time', 'month', order='DESC')


@register.simple_tag
def get_categories():
    return Category.objects.all()


@register.simple_tag
def tags():
    return Tag.objects.all()
