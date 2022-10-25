from django.shortcuts import render

# Create your views here.

#로그인
def signin(request):
    return render(
        request,
        'user/signin.html'
    )

#회원가입
def signup(request):
    return render(
        request,
        'user/signup.html'
    )