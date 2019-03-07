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



############## FORM 验证 #############
from django import forms
from django.forms import widgets
from django.forms import fields
class FM(forms.Form):
    # 这些什么什么field的字段，只能帮我们验证发过来的数据，不能生成html
    # 看他们源码其实内部是做了一个字符串拼接，所以我们加上参数就可以让他自动生成样式
    # 把from换成fields就可以使用插件，
    # widgets插件里啥都有，input，选择框等等
    user = fields.CharField(
        error_messages={'required':'用户名不能为空'},
        widget=widgets.Textarea(attrs={'class':'c1'})
    )
    pwd = fields.CharField(
        max_length=20,
        min_length=6,
        error_messages={'required':'密码不能为空', 'min_length':'密码不能小于6位','max_length':'密码不能大于20位'},
        widget=widgets.PasswordInput(attrs={'class':'c2'}),
    )
    email = fields.EmailField(error_messages={'required':'邮箱不能为空','invalid':'邮箱格式错误'})
    # 单选
    city = fields.ChoiceField(
        choices=[(0, '上海'), (1, '北京'), (2, '深圳')]
    )
    # 多选
    # city2 = fields.MultipleChoiceField(
    #     choices=[(0, '上海'), (1, '北京'), (2, '深圳')]
    # )

from app01 import models
def fm(request):
    if request.method == 'GET':
        # 从数据库获取数据，假设数据是这个，然后把它传入也页面去
        dic = {
            'user':'r1',
            'pwd':'123123',
            'email':'aaa',
            'city':1
        }
        obj = FM(initial=dic)   # 这样就可以传入页面
        return render(request, 'fm.html', {'obj':obj})
    elif request.method == 'POST':
        # 获取用户所有数据
        # 每条数据请求的验证
        # 成功：获取所有的正确的信息
        # 失败：显示错误信息

        # 把POST提交过来的数据传到form表单里
        obj = FM(request.POST)
        # 调用实例化对象的is_valid()方法，帮我做校验
        r1 = obj.is_valid()
        if r1:
            # 校验通过
            # form_obj.cleaned_data <-- 所有有效的数据都存放在cleaned_data属性中
            # user = form_obj.cleaned_data.get("user")
            # pwd = form_obj.cleaned_data.get("pwd")
            # 调用ORM，在数据库中创建新的用户
            # models.UserInfo.objects.create(user=user, pwd=pwd)
            # print(form_obj.cleaned_data)
            models.UserInfo.objects.create(**obj.cleaned_data)  # 直接用obj获取数据然后插入数据库
            # cleaned_data 是可用数据（钩子1）
            # error存放错误信息的钩子
            # is_valid：每一个字段进行正则（内置）+clean_字段：clean（__all__）：_post_clean

        else:
            return render(request, 'fm.html', {'obj':obj})
        return render(request, 'fm.html')