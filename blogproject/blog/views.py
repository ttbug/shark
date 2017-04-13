import markdown
from django.shortcuts import render, get_object_or_404
from .models import Post, Category
# Create your views here.


def index(request):
    post_list = Post.objects.all()
    return render(request, 'blog/index.html', context={
            'post_list': post_list}
    )


def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.body = markdown.markdown(post.body,
            extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
                'markdown.extensions.toc'
            ]
            )
    return render(request, 'blog/detail.html', context={'post': post})


# 处理文章归档
def archives(request, year, month):
    post_list = Post.objects.filter(create_time__year=year, create_time__month=month)
    return render(request, "blog/index.html", context={"post_list": post_list})


# 处理文章标签
def category(request, pk):
    cate = get_object_or_404(Category, pk=pk)
    post_list = Post.objects.filter(category=cate)
    return render(request, "blog/index.html", context={"post_list": post_list})
