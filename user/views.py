from django.shortcuts import render

from django.http.response import HttpResponseRedirect
#from django.urls.base import reverse
from django.urls import reverse
from django.contrib.auth.models import User

from .forms import SigninForm, SignupForm

from django.contrib.auth import login, authenticate, logout
# Create your views here.

#로그인
def signin(request):
    if request.method == "GET":
        return render(
            request,'user/signin.html', {'f':SigninForm()}
        )
    elif request.method == "POST":
        form = SigninForm(request.POST)
        id = request.POST['username']
        pw = request.POST['password']
        u = authenticate(username=id, password=pw)

        if u:  # u에 특정 값이 있다면
            login(request, user=u)  # u 객체로 로그인
            return HttpResponseRedirect(reverse('signin'))
        else:
            return render(request, 'user/signin.html', {'f': form, 'error': '아이디나 비밀번호가 일치하지 않습니다.'})

#로그아웃
def signout(request):
    logout(request)
    return HttpResponseRedirect(reverse('signout'))

#회원가입
def signup(request):
    if request.method == "GET":
        return render(
            request, 'user/signup.html', {'f': SignupForm()}
        )

    elif request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            # cleaned_data는 사용자가 입력한 데이터
            if form.cleaned_data['password'] == form.cleaned_data['password_check']:
                new_user = User.objects.create_user(form.cleaned_data['username'], form.cleaned_data['email'],
                                                    form.cleaned_data['password'])
                new_user.last_name = form.cleaned_data['last_name']
                new_user.first_name = form.cleaned_data['first_name']
                new_user.save()

                return HttpResponseRedirect(reverse('signup'))
            else:
                return render(request, 'user/signup.html', {'f': form, 'error': '비밀번호와 비밀번호 확인이 다릅니다.'})

        else:
            return render(request, 'user/signup.html', {'f': form})


