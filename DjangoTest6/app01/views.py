from django.shortcuts import render

# Create your views here.

from django import forms
from django.forms import fields

from app01 import models


class UserOnfoModelForm(forms.ModelForm):
    class Meta:
        model = models.UserInfo
        fields = '__all__'

class UserInfoForm(forms.Form):
    username = fields.CharField(max_length=32)
    email = fields.EmailField()
    user_type = fields.ChoiceField(
        choices=models.UserType.objects.values_list('id','caption')
    )

    def __init__(self,*args, **kwargs):
        super(UserInfoForm,self).__init__(*args,**kwargs)
        self.fields['user_type'].choices = models.UserType.objects.values_list('id','caption')


def index(request):
    if request.method == 'GET':
        obj = UserInfoForm()
        return render(request, 'index.html', {'obj':obj})
    elif request.method == 'POST':
        obj = UserInfoForm(request.POST)
        obj.is_valid()
        obj.errors
        return render(request, 'index.html',{'obj':obj})
