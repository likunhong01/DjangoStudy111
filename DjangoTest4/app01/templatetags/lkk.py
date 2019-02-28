#coding=utf-8
#Version:python3.6.0
#Tools:Pycharm 2017.3.2
# Author:LIKUNHONG
__date__ = '2019/2/27 21:41'
__author__ = 'likunkun'

from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.simple_tag
def likunkun(a1, a2, a3):
    return a1+a2


@register.filter
def likunhong(a1, a2):  # 最多传两个
    return a1 + a2