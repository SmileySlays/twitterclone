from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View

from tweet.models import Tweet
from tweet.forms import TweetAddForm

from twitteruser.models import TwitterUser

from notification.models import Notification

def tweet_details(request, pk):
    return render(request, "details.html", {"tweet": Tweet.objects.get(pk=pk)})

@method_decorator(login_required, name='dispatch')
class tweet_add_view(View):
    def get(self, request):
        html = "generic_form.html"
        form = TweetAddForm()
        return render(request, html, {'form': form})

    def post(self, request):
        html = "generic_form.html"
        form = TweetAddForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            # Derek helped me out with how to get 
            # who is being notified because I had no idea
            if '@' in data['text']:
                twitterusers = TwitterUser.objects.all()
                for usr in twitterusers:
                    if f'@{usr}' in data['text']:
                        Notification.objects.create(
                            sender = request.user,
                            recipient = usr,
                            message = request.user.username + " tagged you in a tweet!"
                        )
                Tweet.objects.create(
                        text=data['text'],
                        twitteruser=request.user
                        )
            else:
                Tweet.objects.create(
                    text=data['text'],
                    twitteruser=request.user
                )
            return HttpResponseRedirect(reverse("home"))