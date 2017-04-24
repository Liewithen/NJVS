# -*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response
from activity.models import Activity
from news.models import News
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def index(request):
    '''首页'''
    news = News.objects.all()
    
    try:
        page = request.GET.get('page', 1)
    except PageNotAnInteger:
        page = 1


    p = Paginator(news, 2, request=request)

    N = p.page(page)
    return render(request, 'index.html', {'news':N})

def validate(request):
    return render(request, 'validate.html', {})
