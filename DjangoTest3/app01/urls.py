#coding=utf-8
#Version:python3.6.0
#Tools:Pycharm 2017.3.2
# Author:LIKUNHONG
__date__ = '2019/2/18 21:32'
__author__ = 'likunkun'


from django.contrib import admin
from django.urls import path

from django.conf.urls import url
from app01 import views
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^index/', views.index, name='indexx'),    # 写上name，在html页里就可以用模板语言绑定
    url(r'^index2/', views.index2),
    # url(r'^index/(\d+)', views.index, name='indexx'),    # 写上name，在html页里就可以用模板语言绑定
    # 用函数绑定，FBV
    url(r'^login/', views.login),
    url(r'^login2/', views.login2),
    url(r'^orm/', views.orm),

    url(r'^user_info/', views.user_info),
    url(r'^user_detail-(?P<nid>\d+)/', views.user_detail),
    url(r'^user_del-(?P<nid>\d+)/', views.user_del),
    url(r'^user_edit-(?P<nid>\d+)/', views.user_edit),

    # 用类绑定url的写法:CBV
    url(r'^home/', views.Home.as_view()),

    # 路由系统两种方式
    # 不用正则表达式，直接用？nid=后面的拼接来跳转不同信息
    # url(r'^detail/', views.detail),
    # 用正则表达式
    url(r'^detail-(\d+).html', views.detail),
    # 可以传2个
    # url(r'^detail-(\d+)-(\d+).html', views.detail),
    # 还支持正则表达式分组，可以直接吧第一个赋值给nid，第二个赋值给uid
    # url(r'^detail-(?P<nid>\d+)-(?P<uid>\d+).html', views.detail),
]