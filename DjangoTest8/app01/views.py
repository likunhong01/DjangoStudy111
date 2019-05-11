from django.shortcuts import render

# Create your views here.
from app01 import models
def first(request):
    if request.method == 'POST':
        # 前端的登录用户名密码，注册用户名密码
        l_u = request.POST.get('l_u')
        l_p = request.POST.get('l_p')
        r_u = request.POST.get('r_u')
        r_p = request.POST.get('r_p')

        # 如果是登录
        if l_u and l_p:
            right_user = models.Login.objects.get(username=l_u)
            if right_user and right_user.pwd == l_p:
                return render(request, 's.html', {'age':right_user.age})
        
        # 如果是注册

        pass
    elif request.method == 'GET':
        return render(request, 'f.html')

def secend(request):
    return render(request, 's.html')