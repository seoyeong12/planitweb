from django.forms import ModelForm
from django.contrib.auth.models import User
from django import forms

#회원가입을 제공하는 class
class SignupForm(ModelForm):
    password_check = forms.CharField(max_length=200, widget=forms.PasswordInput())
    #password_check는 User에서 정의되지 않음
    field_order = ['username', 'password', 'password_check', 'last_name', 'first_name', 'email']

    class Meta:
        model = User
        widgets = {'password': forms.PasswordInput}
        fields = ['username', 'password', 'last_name', 'first_name', 'email']

#로그인을 제공하는 class
class SigninForm(ModelForm):
    model = User
    widgets = {'password': forms.PasswordInput}
    field = ['username', 'password']