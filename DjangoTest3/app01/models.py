from django.db import models

# Create your models here.

class UserInfo(models.Model):
    # Django会自己创建id列，还是自增的，还是主键



    # 用户名列，字符串，指定长度32
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=64)

    # 在这里重新写表结构后，可以重新生成
    # Django提供了很多种数据类型，不只有字符串，数字，时间，二进制等
    # 还有EmailField,URLField，GenericIP
    # 控制的是Django的admin提交的时候格式是否正确



    # 参数这样使用：
    # password = models.CharField(max_length=64, verbose_name='用户名')