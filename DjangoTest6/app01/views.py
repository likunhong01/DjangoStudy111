from django.shortcuts import render,HttpResponse

# Create your views here.

from django import forms
from django.forms import fields as Ffields, widgets as Fwidgets

from app01 import models

# modelForm的方法
class UserInfoModelForm(forms.ModelForm):

    # 自定义一个单选框
    is_rmb = Ffields.CharField(
        widget=Fwidgets.CheckboxInput()
    )

    class Meta:
        model = models.UserInfo
        fields = '__all__'  # 全有，指定哪个字段
        fields = ['username','email']   # 只要这2个字段
        exclude = ['username']  # 除了这个字段不做验证，其他都做

        # 还有其他参数
        labels = {  # 提示信息
            'username':'用户名',
            'email':'邮箱'
        }
        help_texts = {  # 提示信息
            'username': '要填入用户名',
        }
        # 给加参数样式什么的可以用这个
        widgets = {
            'username': Fwidgets.Textarea(attrs={'class':'c1'}),
        }
        error_messages = {
            '__all__':{

            },
            'email':{
                'required': '邮箱不能为空',
                'invalid': '邮箱格式错误',
            }
        }

        # 字段的类
        # field_classes = {
        #     'email':Ffields.URLField
        # }

        # 时间本地化
        # localized_fields = ('ctime',)

    def clean_username(self):
        old = self.cleaned_data['username']
        # 然后可以改old值，改完了返回
        return old

def index(request):
    if request.method == 'GET':
        # obj = UserInfoForm()  # form写法
        obj = UserInfoModelForm()  # modelform写法
        return render(request, 'index.html', {'obj':obj})
    elif request.method == 'POST':
        # obj = UserInfoForm(request.POST)    # form验证
        obj = UserInfoModelForm(request.POST)    # modelform验证
        # 这三个是一样的，
        # obj.is_valid()
        # obj.errors
        # obj.cleaned_data

        if obj.is_valid():
            obj.save()  # 直接保存到数据库了，不需要自己写
            # 或者拆开这样写3句（源码里可以看）：
            instance = obj.save(False)
            instance.save()
            obj.sava_m2m()


        # models.UserInfo.objects.create(**obj.cleaned_data)
        # models.UserInfo.objects.filter(id=1).update(**obj.cleaned_data)
        return render(request, 'index.html',{'obj':obj})


def user_list(request):
    li = models.UserInfo.objects.all().select_related('user_type','u2g')
    return render(request, 'user_list.html', {'li':li})


def user_edit(request, nid):
    # 获取当前id对象的用户信息
    # 显示用户已经存在的数据
    # 用modelform就很简单了
    if request.method == 'GET':
        user_obj = models.UserInfo.objects.filter(id= nid).first()
        mf = UserInfoModelForm(instance=user_obj)

        return render(request, 'user_edit.html', {'mf':mf,'nid':nid})
    elif request.method == 'POST':
        # 不能这么写，这样不是更改，而是直接保存一个新的在数据库里
        # mf = UserInfoModelForm(request.POST)
        # if mf.is_valid():
        #     mf.save()
        # 要下面这样写，先找到
        user_obj = models.UserInfo.objects.filter(id=nid).first()
        mf = UserInfoModelForm(request.POST, instance=user_obj)
        if mf.is_valid():
            mf.save()
        else:
            print(mf.errors.as_join())
        return render(request, 'user_edit.html',{'mf':mf, 'nid':nid})


# Form和models分开的form写法
class UserInfoForm(forms.Form):
    username = Ffields.CharField(max_length=32)
    email = Ffields.EmailField()
    user_type = Ffields.ChoiceField(
        choices=models.UserType.objects.values_list('id','caption')
    )

    def __init__(self,*args, **kwargs):
        super(UserInfoForm,self).__init__(*args,**kwargs)
        self.fields['user_type'].choices = models.UserType.objects.values_list('id','caption')


# def index(request):
#     if request.method == 'GET':
#         # obj = UserInfoForm()  # form写法
#         obj = UserInfoModelForm()  # modelform写法
#         return render(request, 'index.html', {'obj':obj})
#     elif request.method == 'POST':
#         # obj = UserInfoForm(request.POST)    # form验证
#         obj = UserInfoModelForm(request.POST)    # modelform验证
#         obj.is_valid()
#         obj.errors
#         # models.UserInfo.objects.create(**obj.cleaned_data)
#         # models.UserInfo.objects.filter(id=1).update(**obj.cleaned_data)
#         return render(request, 'index.html',{'obj':obj})


################## AJAX #####################
def ajax(request):
    return render(request, 'ajax.html')

def ajax_json(request):
    ret = {'status': True, 'data':None}
    import json
    return HttpResponse(json.dumps(ret))


# 上传文件
def upload(request):
    return render(request,'upload.html')

def upload_file(request):
    username = request.POST.get('username')
    fafafa = request.FILES.get('fafafa')
    import os
    img_path = os.path.join('static/imgs/',fafafa.name)
    with open(img_path, 'wb') as f:
        for item in fafafa.chunks():
            f.write(item)
    ret = {'code':True, 'data': img_path}
    import json
    return HttpResponse(json.dumps(ret))