from django.db import models

# Create your models here.

class UserType(models.Model):
    caption = models.CharField(max_length=32)

class UserGroup(models.Model):
    name = models.CharField(max_length=32)


class UserInfo(models.Model):
    # username = models.CharField(max_length=32)
    # 如果用modelform的形式，要写verbosename=用户名
    username = models.CharField(verbose_name='用户名', max_length=32)
    email = models.EmailField()
    user_type = models.ForeignKey(to='UserType', to_field='id',on_delete=models.CASCADE)
    u2g = models.ManyToManyField(UserGroup)
