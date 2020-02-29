from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from tweet.models import Tweet
from twitteruser.models import TwitterUser

@login_required()
def home(request):
    users = TwitterUser.objects.get(twitteruser=request.user)
    tweets = Tweet.objects.filter(twitteruser=request.user)
    user_tweets = Tweet.objects.all().exclude(twitteruser=request.user)
    print(tweets)
    return render(request, "home.html", 
                    {"tweets": tweets,
                    "users": users,
                    'user_tweets': user_tweets})