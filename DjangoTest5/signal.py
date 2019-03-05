#coding=utf-8
#Version:python3.6.0
#Tools:Pycharm 2017.3.2
# Author:LIKUNHONG
__date__ = '2019/3/4 23:39'
__author__ = 'likunkun'

# 自定义信号：
import django.dispatch
pizza_done = django.dispatch.Signal(providing_args=["toppings", "size"])


def callback(sender, **kwargs):
    print("callback")
    print(sender, kwargs)

pizza_done.connect(callback)