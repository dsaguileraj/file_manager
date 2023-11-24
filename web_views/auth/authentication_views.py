from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.gzip import gzip_page

from api.v1.authentication.services.auth_service import AuthService


@gzip_page
def logout_view(request, lang=None):
    if not request.session.is_empty():
        logout(request)
    return HttpResponseRedirect("/login/")


@gzip_page
def login(request):
    srv = AuthService()
    template = "auth/login.html"
    print(request.session)
    print(request.session)
    print(request.session.get("username"))
    print(request.session.get("token"))
    if not request.session.is_empty():
        return HttpResponseRedirect("/management/")
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        if token := srv.login(username=username,
                              password=password):
            request.session["username"] = username
            request.session["token"] = token.key
            return HttpResponseRedirect("/management/")
        return render(request, template, {"error": True})
    elif request.method == "GET":
        return render(request, template)


@gzip_page
def signup(request):
    srv = AuthService()
    template = "auth/signup.html"
    if not request.session.is_empty():
        return HttpResponseRedirect("/management/")
    if request.method == "POST":
        username = request.POST.get("username", "")
        email = request.POST.get("email", "")
        password = request.POST.get("password", "")
        if token := srv.signup(username=username,
                               password=password,
                               email=email):
            request.session["username"] = username
            request.session["token"] = token.key
            return HttpResponseRedirect("/management/")
        return render(request, template, {"error": True})
    elif request.method == "GET":
        return render(request, template)
