from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from notification.models import Notification

@login_required()
def notifications(request):
    notifications = Notification.objects.filter(recipient=request.user)

    for notification in notifications:
        if notification.read == False:
            notification.read = True
            notification.save()

    return render(request, "notifications.html", 
                {"notifications": notifications})
