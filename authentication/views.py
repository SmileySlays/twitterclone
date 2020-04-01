from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib.auth import login, authenticate, logout
from django.views import View

from authentication.forms import LoginForm, SignupForm
from twitteruser.models import TwitterUser

class signup_view(View):
    def get(self, request):
        html = "signup.html"
        form = SignupForm()
        return render(request, html, {'form': form})

    def post(self, request):
        html = "signup.html"
        form = SignupForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = TwitterUser.objects.create_user(
                username=data['username'],
                password=data['password']
            )
            login(request, user)
            return HttpResponseRedirect("/home/")

class login_view(View):
    def get(self, request):
        html = "login.html"
        form = LoginForm()
        return render(request, html, {'form': form})

    def post(self, request):
        html = "login.html"
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(username=data['username'], password=data['password'])
            login(request, user)
            if user is not None:
                login(request, user)
                # Where we want to go next after logging in correctly
                return HttpResponseRedirect("/home/")

class logout_view(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect("/")