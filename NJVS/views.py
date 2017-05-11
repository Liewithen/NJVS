# -*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response
from activity.models import Activity
from news.models import News, Banner
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def index(request):
    '''首页'''
    banner = Banner.objects.all()[:4]
    return render(request, 'index.html', {'banners':banner})
