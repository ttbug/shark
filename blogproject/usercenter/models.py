from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class ActivateCode(models.Model):
    user = models.ForeignKey(User, verbose_name="用户")
    code = models.CharField("激活码", max_length=100)

    expire_timestamp = models.DateTimeField()

    create_timestamp = models.DateTimeField(auto_now_add=True)
    last_update_timestamp = models.DateTimeField(auto_now=True)
