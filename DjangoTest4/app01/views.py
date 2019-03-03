from django.http import HttpResponse
from django.shortcuts import render,redirect

# Create your views here.
from app01 import models


def tpl1(request):
    return render(request, '继承master.html')

def tpl2(request):
    return render(request, '引入tag.html')

def tpl3(request):
    return render(request, 'tpl3.html')

import json
def login(request):
    Users = models.User.objects.all()
    username = []
    for i in Users:
        username.append(i.username)
    return render(request, "login.html",{'username': json.dumps(username)})



LIST = []
for i in range(109):
    LIST.append(i)

from utils import pagination
def user_list(request):
    current_page = int(request.GET.get('p',1))
    page_obj = pagination.Page(current_page, len(LIST))
    data = LIST[page_obj.start:page_obj.end]
    page_str = page_obj.page_str("/user_list/")

    return render(request, 'user_list.html', {'li':data, 'page_str':page_str})




# ----------------------------cookie------------------

def cookie(request):
    # 获取cookie
    request.COOKIES
    request.COOKIES['username111']
    request.COOKIES.get('username111')

    # 设置cookie
    response = render(request, 'index.html')
    response = redirect('/index/')
    # 设置cookie，关闭浏览器就失效
    response.set_cookie('key', 'value')
    # 设置cookie，N秒后失效
    response.set_cookie('username111','value',max_age=100)

    # 自定义时间删除cookie
    import datetime
    current_data = datetime.datetime.utcnow()
    current_data = current_data + datetime.timedelta(seconds=500)
    # 转换成时间的截止日期传进去
    response.set_cookie('username111', 'value', expires=current_data)


    # cookie加密，用aaaa方式加密
    obj = HttpResponse('s')
    obj.set_signed_cookie('username111', 'lkk', salt="aaaa")
    # cookie解密也得用aaaa解密
    request.get_signed_cookie('username111', salt='aaaa')



    return response



'''装饰器'''
def auth(func):
    def inner(request, *args, **kwargs):
        v = request.COOKIES.get('username111')
        if not v:
            return redirect('/login/')
        return func(request, *args, **kwargs)
    return inner


# FBV模式:function
@auth
def loginnn(request):
    pass

# CBV模式:class
from django import views
from django.utils.decorators import method_decorator

# 在类里有3种写法可以让他变成有装饰器功能
# 第一个是用method_decorator，在要装饰的函数上写@method_decorator(auth)
# 第二个是写一个dispatch函数，再用method_decorator装饰上，可以让全部函数都被装饰
# 第三个是直接在类上写@method_decorator(auth,name='dispatch')
@method_decorator(auth,name='dispatch')
class Oreder(views.View):
    @method_decorator(auth)
    def dispatch(self, request, *args, **kwargs):
        return super(Oreder, self).dispatch(request, *args, **kwargs)

    @method_decorator(auth)
    def get(self, request):
        v = request.COOKIES.get('username111')
        return render(request, 'index.html', {'current_user':v})

    @method_decorator(auth)
    def post(self, request):
        v = request.COOKIES.get('username111')
        return render(request, 'index.html', {'current_user': v})
