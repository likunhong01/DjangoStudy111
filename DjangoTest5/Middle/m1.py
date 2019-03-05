#coding=utf-8
#Version:python3.6.0
#Tools:Pycharm 2017.3.2
# Author:LIKUNHONG
__date__ = '2019/3/4 22:00'
__author__ = 'likunkun'

from django.utils.deprecation import MiddlewareMixin

class Row1(MiddlewareMixin):
    def process_request(self,request):
        print('request1')

    def process_view(self, request, view_func, view_func_args, view_func_kwargs):
        print('view1')

    def process_response(self, request, response):
        print('response1')
        return response

from django.shortcuts import HttpResponse
class Row2(MiddlewareMixin):
    def process_request(self,request):
        print('request2')
        # return HttpResponse('走')

    def process_view(self, request, view_func, view_func_args, view_func_kwargs):
        print('view2')

    def process_response(self, request, response):
        print('response2')
        return response

class Row3(MiddlewareMixin):
    def process_request(self,request):
        print('request3')

    def process_view(self, request, view_func, view_func_args, view_func_kwargs):
        print('view3')

    def process_response(self, request, response):
        print('response3')
        return response

    def process_exception(self, request, exception):
        if isinstance(exception,ValueError):
            return HttpResponse('出现异常》。。')

    def process_template_response(self,request,response):
        # 如果Views中的函数返回的对象中，具有render方法，就会触发
        print('-----------------------')
        return response