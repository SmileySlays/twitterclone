from django.shortcuts import render, HttpResponseRedirect, reverse

from tweet.models import Tweet
from tweet.forms import TweetAddForm


def tweet_add_view(request):
    html = "generic_form.html"

    if request.method == "POST":
        form = TweetAddForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Tweet.objects.create(
                text=data['text'],
                twitteruser=request.user
            )
            return HttpResponseRedirect(reverse("home"))

    form = TweetAddForm()

    return render(request, html, {'form': form})