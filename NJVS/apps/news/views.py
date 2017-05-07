from django.shortcuts import render
from django.views.generic import View
from news.models import News
from django.http import HttpResponseRedirect
# Create your views here.

class NewsView(View):
    def get(self, request):
        id = request.GET.get('id')
        if id == "":
            HttpResponseRedirect('/')
        news = News.objects.get(id=id)
        return render(request, 'news/news.html', {'news':news})