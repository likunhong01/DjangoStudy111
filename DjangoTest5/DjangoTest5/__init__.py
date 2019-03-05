from django.core.signals import request_finished
from django.core.signals import request_started
from django.core.signals import got_request_exception

from django.db.models.signals import class_prepared
from django.db.models.signals import pre_init, post_init
from django.db.models.signals import pre_save, post_save
from django.db.models.signals import pre_delete, post_delete
from django.db.models.signals import m2m_changed
from django.db.models.signals import pre_migrate, post_migrate

from django.test.signals import setting_changed
from django.test.signals import template_rendered

from django.db.backends.signals import connection_created


def callback(sender, **kwargs):
    # sender里是信号的所有信息
    print("callback")
    print(sender, kwargs)

# 这样就添加上了，在进行数据库查询前就会触发callback函数
# 还可以用上面的各种（前后触发等等）
pre_init.connect(callback)


