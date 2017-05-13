from django.conf.urls import url, include
from . import views


app_name = "usercenter"
urlpatterns = [
    url(r'^register$', views.register, name="register"),
    url(r'^activate/(?P<code>\w+)', views.activate, name="activate"),
    url(r'^accounts/', include("django.contrib.auth.urls")),
]
