from django.shortcuts import render,redirect

# Create your views here.

from django.shortcuts import HttpResponse
import os

USER_DICT = {
    '1':{'name': 'root1','email':'1@163.com'},
    '2':{'name': 'root2','email':'2@163.com'},
    '3':{'name': 'root3','email':'3@163.com'},
    '4':{'name': 'root4','email':'4@163.com'},
    '5':{'name': 'root5','email':'5@163.com'},

}
USER_LIST = [
    {'name': 'root1'},
    {'name': 'root2'},
    {'name': 'root3'},
]


def user_detail(request, nid):
    obj = models.UserInfo.objects.filter(id=nid).first()
    # models.UserInfo.objects.get(id=nid)   # 这句可能会报错要用try
    return render(request, 'user_detail.html', {'obj':obj})

def user_del(request, nid):
    models.UserInfo.objects.filter(id = nid).delete()
    # return redirect('/cmdb/user_info/')
    return redirect('/cmdb/user_info/')

def user_edit(request, nid):
    if request.method == 'GET':
        obj = models.UserInfo.objects.filter(id= nid).first()
        return render(request, 'user_edit.html', {'obj':obj})
    elif request.method == 'POST':
        nid = request.POST.get('id')
        u = request.POST.get('username')
        p = request.POST.get('password')
        print(nid)
        obj = models.UserInfo.objects.filter(id = nid).update(username=u, password=p)
        print(obj)
        return redirect('/cmdb/user_info/')


def user_info(request):
    if request.method == "GET":
        user_list = models.UserInfo.objects.all()   # 是QuerySet类型,里面是对象
        return render(request, 'user_info.html', {'user_list':user_list})
    elif request.method == "POST":
        u = request.POST.get('user')
        p = request.POST.get('pwd')
        models.UserInfo.objects.create(username=u,password=p)

        return redirect('/cmdb/user_info/')



def index(request, nid):
    from django.urls import reverse
    v = reverse('indexx', args=(90,))   # 可以自动生成url
    v = reverse('indexx', kwargs={nid : 90})   # 可以自动生成url
    return render(request, 'index.html', {'user_dict': USER_DICT})


def index2(request):
    return render(request, 'index2.html')






# def login(request):
#     if request.method == 'GET':
#         return render(request,'login.html')
#     elif request.method == 'POST':
#         u = request.POST.get('user')
#         p = request.POST.get('123')
#         if u == 'lkk' and p == '123':
#             return redirect('/index/')
#         else:
#             return render(request, 'login.html')
#     else:
#         return redirect('/index')



'''路由系统2种'''
# # 不用正则表达式
# def detail(request):
#     nid = request.GET.get('nid')
#     detail_info = USER_DICT[nid]
#     return render(request, 'detail.html', {'detail_info': detail_info})

# 用正则表达式
# 用正则表达式也可以2个参数,是按顺序来的
def detail(request, nid):
# def detail(request, *args ,**kargs):  # 这样写可以不用在意html里写了几个参数，都能接受到
    detail_info = USER_DICT[nid]
    print(nid)
    return render(request, 'detail.html', {'detail_info': detail_info})


# 连接数据库的操作
def login2(request):
    if request.method == 'GET':
        return render(request,'login2.html')
    elif request.method == 'POST':
        # 从数据库中执行select * from user where
        u = request.POST.get('user')
        p = request.POST.get('pwd')
        # obj = models.UserInfo.objects.filter(username=u, password=p)

        # count = models.UserInfo.objects.filter(username=u, password=p).count()

        obj = models.UserInfo.objects.filter(username=u, password=p).first()

        if obj:
            return redirect('/cmdb/index2/')
        else:
            return render(request,'login2.html')
    else:
        return redirect('')



from app01 import models
def orm(request):
    # -----------创建---------------
    # 方法1：
    models.UserInfo.objects.create(username='root', password='123')
    # 方法2：
    # dic = {'username':'root', 'password':'123'}
    # models.UserInfo.objects.create(**dic)
    # 方法3：
    # obj = models.UserInfo(username='lkk', password='123')
    # obj.save()

    # 查
    result = models.UserInfo.objects.all()  # 查所有
    # 返回QuerySet:是Django提供的一个类型，可以当作一个列表[]
    # 列表里有[obj, obj, obj]可以用迭代器for循环显示出来
    # result = models.UserInfo.objects.filter(username='root', password='123')  # 按条件查，得到的也是QuerySet

    # 删
    models.UserInfo.objects.filter(username='lkk').delete()

    #改（更新）
    models.UserInfo.objects.filter(username='lkk').update(password='lkk123')

    return HttpResponse('orm')



def login(request):
    if request.method == 'GET':
        return render(request,'login.html')
    elif request.method == 'POST':
        v = request.POST.get('gender')  # 获取性别
        # 获取CheckBox像上面一样，get只能获取一个，要用getlist
        cb = request.POST.getlist('favor')
        print(cb)

        # 取上传的文件------------
        fobj = request.FILES.get('fa')
        file_path = os.path.join('upload',fobj.name)
        # 然后要chunks:
        f = open(file_path, mode="wb")
        for i in fobj.chunks():
            f.write(i)
        f.close()

        return render(request, 'login.html')
    else:
        return redirect('/index')



# 用类的写法CBV
from django.views import View
class Home(View):
    # get请求调用get方法
    # post请求调用post方法
    # 可以调用的有：不同方式提交
    # http_method_names = ['get', 'post', 'put', 'patch', 'delete', 'head', 'options', 'trace']

    # 如果自己写了dispatch并且return就会自动先执行这个，以下代码一个都不会执行
    def dispatch(self, request, *args, **kwargs):
        # 可以使用super，调用父类中的dispatch方法
        # 其实类似装饰器
        print('before')
        result = super(Home, self).dispatch(request, *args, **kwargs)
        print('after')
        return result

    def get(self, request):
        print(request.method)
        return render(request, 'home.html')

    def post(self, request):
        print(request.method)
        return render(request, 'home.html')


