from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib.auth import login, authenticate 

from authentication.forms import LoginForm, SignupForm
from twitteruser.models import TwitterUser

def signup_view(request):
    html = "signup.html"

    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = TwitterUser.objects.create_user(
                data['username'],
                data['password']
            )
            TwitterUser.objects.create(
            )
            login(request, user)
            return HttpResponseRedirect("/home/")

    else:
        form = SignupForm()
    return render(request, html, {'form': form})

def login_view(request):
    html = "login.html"

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(username=data['username'], password=data['password'])
            login(request, user)
            if user is not None:
                login(request, user)
                # Where we want to go next after logging in correctly
                return HttpResponseRedirect("/home/")
    else:
        form = LoginForm()
    return render(request, html, {'form': form})