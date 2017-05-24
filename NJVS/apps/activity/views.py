from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from datetime import datetime, date
from django.views.generic import View
from .models import Activity, EnterList
from users.models import VTeam
from .forms import ApplyActForm
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from string import strip
from datetime import date
# Create your views here.
mon = {
    'January': 1,
    'February': 2,
    'March': 3,
    'April': 4,
    'May': 5,
    'June': 6,
    'July': 7,
    'August': 8,
    'September': 9,
    'October': 10,
    'November': 11,
    'December': 12
}

def changeTime(line):
    tmp = line.split(',')
    year = int(strip(tmp[1]))
    tmp = tmp[0].split(' ')
    day = int(tmp[0])
    month = mon[tmp[1]]
    return date(year, month, day)


class ActivityView(View):
    def get(self, request):
        acts_f = Activity.objects.filter(is_finished=True).order_by('-application_time')
        acts_w = Activity.objects.filter(is_finished=False).order_by('-application_time')
        return render(request, 'activity/activity.html', {
            'acts_f': acts_f,
            'acts_w': acts_w
        })


class ActProfileView(View):
    def get(self, request):
        id = request.GET.get("id")
        act = Activity.objects.get(activity_id=id)
        return render(request, 'activity/actprofile.html', {'act': act})


class ApplyActView(View):
    @method_decorator(login_required)
    def post(self, request):
        form = ApplyActForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            team_id = request.user.team_id
            team_name = VTeam.objects.get(team_id=team_id).team_name
            Activity.objects.create(
                activity_name = cd['activity_name'],
                team_id = team_id,
                team_name = team_name,
                contact_qq = cd['contact_qq'],
                contact_phone = cd['contact_phone'],
                start_time = changeTime(cd['start_time']),
                end_time = changeTime(cd['end_time']),
                place = cd['place'],
                time_detail = cd['time_detail'],
                per_time= cd['per_time'],
                days= cd['days'],
                weeks = cd['weeks'],
                need_number = cd['need_number'],
                details = cd['details']
            )
            return HttpResponseRedirect('/activity/')
        else:
            return HttpResponseRedirect('/teamprofile/?err=1')
            


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

def addStuTime(request):
    if request.is_ajax():
        data = eval(request.POST.get('data'))
        act_id = data['id']
        act = Activity.objects.get(activity_id=act_id)
        if act.is_finished:
            return HttpResponse('error', content_type="application/text")
        stus = data['list']
        for stu in stus:
            tmp = EnterList.objects.get(activity_id=act_id, participant=stu['username'])
            tmp.v_time = stu['time']
            tmp.save()    
        act.is_finished = True
        act.save()        
        return HttpResponse('ok', content_type="application/text")
