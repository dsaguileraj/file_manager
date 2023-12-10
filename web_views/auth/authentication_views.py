from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.gzip import gzip_page
from django.contrib.auth import authenticate, login
from api.v1.authentication.services.auth_service import AuthService


@gzip_page
def logout_view(request, lang=None):
    if not request.session.is_empty():
        logout(request)
    return HttpResponseRedirect("/auth/login/")


@gzip_page
def login_view(request):
    srv = AuthService()
    template = "auth/login.html"
    if request.user.is_authenticated:
        return HttpResponseRedirect("/management/file/")
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        token, user = srv.login(username=username,
                                password=password)
        if user and token:
            request.session["id"] = user.id
            request.session["username"] = user.username
            request.session["token"] = token.key
            login(request, user)
            return HttpResponseRedirect("/management/file/")
        return render(request, template, {"error": True})
    elif request.method == "GET":
        return render(request, template)


@gzip_page
def signup_view(request):
    srv = AuthService()
    template = "auth/signup.html"
    if request.user.is_authenticated:
        return HttpResponseRedirect("/management/file/")
    if request.method == "POST":
        username = request.POST.get("username", "")
        email = request.POST.get("email", "")
        password = request.POST.get("password", "")
        token, user = srv.signup(username=username,
                                 password=password,
                                 email=email)
        if token and user:
            request.session["id"] = user.id
            request.session["username"] = username
            request.session["token"] = token.key
            login(request, user)
            return HttpResponseRedirect("/management/file/")
        return render(request, template, {"error": True})
    elif request.method == "GET":
        return render(request, template)
