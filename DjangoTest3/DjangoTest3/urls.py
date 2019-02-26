"""DjangoTest3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
# from django.urls import path

from django.conf.urls import url, include
# from app01 import views

# 路由分发
urlpatterns = [
    url(r'^cmdb/', include("app01.urls")),
    # url(r'^monitor/', include("app02.urls")),
]

"""
urlpatterns = [
    path('admin/', admin.site.urls),
    # url(r'^index/', views.index, name='indexx'),    # 写上name，在html页里就可以用模板语言绑定
    url(r'^index/(\d+)', views.index, name='indexx'),    # 写上name，在html页里就可以用模板语言绑定
    # 用函数绑定，FBV
    url(r'^login/', views.login),

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
"""



