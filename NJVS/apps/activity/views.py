from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime, date
from django.views.generic import View
from .models import Activity, EnterList
# Create your views here.


class ActivityView(View):
    def get(self, request):
        act = Activity.objects.all()
        return render(request, 'activity/activity.html', {'acts': act})


class ActProfileView(View):
    def get(self, request):
        id = request.GET.get("id")
        act = Activity.objects.get(activity_id=id)
        return render(request, 'activity/actprofile.html', {'act': act})

def joinActivity(request):
    if request.is_ajax():
        if not request.user.is_authenticated():
            result = 3
            return HttpResponse(result, content_type="application/text")
        username = request.user.username
        realname = request.user.real_name
        act_id = request.GET.get('id')
        act = Activity.objects.get(activity_id=act_id)
        try:
            EnterList.objects.get(participant=username, activity_id=int(act_id))
            result = 0
            return HttpResponse(result, content_type="application/text")
        except EnterList.DoesNotExist:
            if act.join_number >= act.need_number:
                result = 2
                return HttpResponse(result, content_type="application/text")
            act_name = act.activity_name
            act.join_number += 1
            act.save()
            EnterList.objects.create(activity_id=int(act_id),
            participant = username,
            p_name = realname,
            activity = act_name
            )
            result = 1
            return HttpResponse(result, content_type="application/text")
