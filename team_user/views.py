from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, resolve_url
from django.contrib.auth import authenticate, login
from django.urls import reverse


# Create your views here.
def signup(request):
    if request.method == "POST":
        user_name = request.POST['userName']
        first_name = user_name[0]
        last_name = user_name[1:]
        new_user = User.objects.create_user(username = request.POST['userId'],
                                            password = request.POST['userPsw'],
                                            email = request.POST['userEmail'],
                                            first_name = first_name,
                                            last_name = last_name)
        new_user.save()
        return HttpResponseRedirect(resolve_url('signup'))
    else:
        return render(request,
                      'team_user/signup.html',
                      )


"""
def signin(request):
    if request.method =="POST":
        username = request.POST["userId"]
        password = request.POST["userPsw"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if request.POST.get("keep_login") =="True":
                response = redirect('userPage')
                response.set_cookie('username', username)
                response.set_cookie('password', password)
                return response
                #return redirect('userPage')
        else:
            return redirect('index')
"""
"""
def userPage(request):
    user = User.objects.get(username=request.COOKIES.get('username'))
    pageContext = {'user':user}
    return render(request, 'signup/team_user.html', pageContext)
"""
"""
def signout(request):
    response = redirect('index')
    response.delete_cookie('username')
    response.delete_cookie('password')
    logout(request)
    return response
"""
"""
def index(request):
    if request.COOKIES.get('username') is not None:
        response = render(request, 'signinApp/index.html')
        response.delete_cookie('username')
        response.delete_cookie('password')
        logout(request)
        return response
"""