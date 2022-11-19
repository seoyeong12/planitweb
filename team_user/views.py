from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, resolve_url
from django.contrib.auth import authenticate, login, logout

from django.urls import reverse
from django.views.generic import RedirectView


# Create your views here.

#메인
def main(request):
    return render(request,
                  'team_user/main.html',
                  )

#회원가입
def signup(request):
    if request.method == "POST":
        user_name = request.POST['userName']
        first_name = user_name[1:]
        last_name = user_name[0]
        new_user = User.objects.create_user(username = request.POST['userId'],
                                            password = request.POST['userPsw'],
                                            email = request.POST['userEmail'],
                                            first_name = first_name,
                                            last_name = last_name)
        new_user.save()
        return HttpResponseRedirect(resolve_url('signin'))
    else:
        return render(request,
                      'team_user/signup.html',
                      )


#로그인
def signin(request):
    if request.COOKIES.get('username') is not None:
        username = request.COOKIES.get('username')
        password = request.COOKIES.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('../../single') #이동 페이지
        else:
            return render(request, "team_user/signin.html")

    elif request.method == "POST":
        username = request.POST["userId"]
        password = request.POST["userPsw"]
        user = authenticate(request, username=username, password=password)
        if user is not None: #해당되는 유저가 있다면
            login(request, user)
            if request.POST.get("keep_login") == "True":
                response = render(request, 'single/schedule_form.html')
                #response = redirect('signin')
                response.set_cookie('username', username)
                response.set_cookie('password', password)
                return response
                #return HttpResponseRedirect(resolve_url('signin'))
                #return redirect('userPage')
            return redirect('../../single')
        else:
            return render(request, 'team_user/signin.html', {'error': 'username or password is incorrect'})
    return render(request, 'team_user/signin.html')


#로그아웃
def signout(request):
    if request.method == 'POST':
        logout(request)
        return redirect('plan_it')
    return render(request,
                  'team_user/main.html')


"""
참고용
def userPage(request):
    user = User.objects.get(username=request.COOKIES.get('username'))
    pageContext = {'user':user}
    return render(request, 'signup/team_user.html', pageContext)
"""


"""
#참고
def single(request):
    if request.COOKIES.get('username') is not None:
        response = render(request, 'signin.html')
        response.delete_cookie('username')
        response.delete_cookie('password')
        logout(request)
        return response
"""