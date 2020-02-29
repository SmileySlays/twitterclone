from django import forms
from twitteruser.models import TwitterUser

class TweetAddForm(forms.Form):
    text = forms.CharField(max_length=140)