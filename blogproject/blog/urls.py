from django.conf.urls import url
from . import views


# 告诉 django 这个 urls.py 模块是属于 blog 应用
app_name = 'blog'
urlpatterns = [
            url(r'^$', views.index, name="index"),
            url(r'^post/(?P<pk>[0-9]+)/$', views.detail, name="detail"),
        ]
