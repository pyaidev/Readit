from django.shortcuts import render
from .models import FeedBack


def about(request):
    feeds = FeedBack.objects.all()
    context = {
        'object_list': feeds
    }
    return render(request, 'about.html', context)
