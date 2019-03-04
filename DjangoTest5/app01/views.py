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