from django.shortcuts import render
from django.views.generic import View
# Create your views here.

class ActivityView(View):

    def get(self, request):
        return render(request, 'activity/activity.html', {})