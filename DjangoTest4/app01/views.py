from django.shortcuts import render

# Create your views here.


def tpl1(request):
    return render(request, 'tpl1.html')

def tpl2(request):
    return render(request, 'tpl2.html')

def tpl3(request):
    return render(request, 'tpl3.html')





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