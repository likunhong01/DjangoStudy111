from django.http import HttpResponse
from django.shortcuts import render,redirect


# Create your views here.

def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        user = request.POST.get('user')
        pwd = request.POST.get('pwd')
        print(user,pwd)
        if user == 'root' and pwd == '123':
            # session中设置
            request.session['username'] = user
            request.session['is_login'] = True
            return redirect('/index/')
        else:
            return render(request, 'login.html')

# # 额外设置要不要csrf保护
# from django.views.decorators.csrf import csrf_exempt,csrf_protect
# @csrf_exempt    # 不验证
# @csrf_protect   #验证
def index(request):
    # session中获取值
    if request.session['is_login']:
        return HttpResponse(request.session['username'])
    else:
        return HttpResponse('无法登陆')


class Foo:
    def render(self):
        return HttpResponse('ok')

def test(request):
    int('aaa')
    print('真正的函数')
    return Foo()

# 页面级别缓存，视图函数级别整体缓存
from django.views.decorators.cache import cache_page
# @cache_page(10) # 缓存10秒，之后就会刷新
def cache(request):
    import time
    ctime = time.time()
    return render(request, 'cache.html', {'ctime': ctime})


def signal(request):
    from app01 import models

    # Django已经给留好了位置，给执行数据库查询的前后可以加各种操作。
    # 只需要在项目下的init里写内容（去init看）
    obj = models.UserInfo(user='root')

    obj.save()


    obj = models.UserInfo(user='root')
    obj.save()

    obj = models.UserInfo(user='root')
    obj.save()


    # 触发自定义信号
    from signal import pizza_done
    pizza_done.send(sender='seven', toppings=123, size=456)
    #
