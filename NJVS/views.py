# -*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response


# Create your views here.
def index(request):
    '''首页'''
    return render(request, 'index.html', {})

def validate(request):
    return render(request, 'validate.html', {})
