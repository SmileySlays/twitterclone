from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from tweet.models import Tweet
from twitteruser.models import TwitterUser
from notification.models import Notification

@login_required(login_url='/login/')
def home(request):
    users = TwitterUser.objects.get(twitteruser=request.user)
    tweets = Tweet.objects.filter(twitteruser=request.user)
    user_tweets = Tweet.objects.all().exclude(twitteruser=request.user)
    notifications = Notification.objects.filter(recipient=request.user).exclude(read=True)
    print(tweets)
    return render(request, "home.html", 
                    {"tweets": tweets,
                    "users": users,
                    'user_tweets': user_tweets,
                    "notifications": notifications})