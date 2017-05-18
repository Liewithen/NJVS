# -*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response
from activity.models import Activity
from news.models import News, Banner
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger


def index(request):
    banner = Banner.objects.all()[:4]
    news = News.objects.all().order_by('-add_time')[:10]
    activity = Activity.objects.all().order_by('-start_time')[:5]
    return render(request, 'index.html', {
        'banners': banner,
        'news': news,
        'acts': activity
        })
