from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth.decorators import login_required

from tweet.models import Tweet
from twitteruser.models import TwitterUser


def twitteruser(request, twitteruser):
    twitteruser = TwitterUser.objects.get(username=twitteruser)
    tweets = Tweet.objects.filter(twitteruser=twitteruser)
    return render(request, "twitterusers.html", 
                    {"tweets": tweets,
                    "twitteruser": twitteruser})

@login_required()
def follow_add_view(request, twitteruser):
    follower = TwitterUser.objects.get(username=twitteruser)
    loggedin_user = TwitterUser.objects.get(username=request.user)
    loggedin_user.follows.add(follower)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required()
def follow_remove_view(request, twitteruser):
    follower = TwitterUser.objects.get(username=twitteruser)
    loggedin_user = TwitterUser.objects.get(username=request.user)
    loggedin_user.follows.remove(follower)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required()
def follow_view(request, twitteruser):
    twitteruser = TwitterUser.objects.get(username=twitteruser)
    following = twitteruser.follows.all()
    return render(request, "following.html", 
                    {"twitteruser": twitteruser,
                     "following": following})