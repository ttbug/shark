from django.shortcuts import render, get_object_or_404
from .models import Post, Category, Tag
from django.conf import settings
from utils.paginator import paginate_queryset
# Create your views here.


def index(request):
    post_list = Post.objects.all().order_by("-id")
    page_no = int(request.GET.get("page_no", "1"))
    page_articles, pagination_data = paginate_queryset(post_list, page_no)
    return render(request, 'blog/index.html', context={
        'post_list': page_articles, 'pagination_data': pagination_data}
    )


def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/detail.html', context={'post': post})


# 处理文章归档
def archives(request, year, month):
    post_list = Post.objects.filter(create_time__year=year, create_time__month=month)
    return render(request, "blog/index.html", context={"post_list": post_list})


# 处理文章标签
def category(request, pk):
    cate = get_object_or_404(Category, pk=pk)
    post_list = Post.objects.filter(category=cate).order_by("id")
    page_no = int(request.GET.get("page_no", "1"))
    page_articles, pagination_data = paginate_queryset(post_list, page_no)
    return render(request, "blog/index.html", context={"post_list": page_articles,
        "pagination_data": pagination_data})


def tags(request, pk):
    label = get_object_or_404(Tag, pk=pk)
    post_list = Post.objects.filter(tags=label).order_by("-id")
    page_no = int(request.GET.get("page_no", "1"))
    page_articles, pagination_data = paginate_queryset(post_list, page_no)
    return render(request, "blog/index.html", context={"post_list": page_articles,
        "pagination_data": pagination_data})


def global_settings(request):
    return {
            "SITE_NAME": settings.SITE_NAME,
            "SITE_DESC": settings.SITE_DESC,
            "CONNECT": settings.CONNECT,
    }


def search(request):
    key = request.GET.get("key")
    err_msg = ""

    if not key:
        err_msg = "请输入关键词"
        return render(request, 'blog/errors.html', {"err_msg": err_msg})

    post_list = Post.objects.filter(title__icontains=key)
    return render(request, 'blog/results.html', {"err_msg": err_msg, "post_list": post_list})
