from django.shortcuts import render

# Create your views here.


def tpl1(request):
    return render(request, 'tpl1.html')

def tpl2(request):
    return render(request, 'tpl2.html')

def tpl3(request):
    return render(request, 'tpl3.html')