# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.views.generic.base import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .forms import LoginForm
from .models import TeamUser, VTeam
from activity.models import Activity, EnterList


class LoginView(View):
    def get(self, request):
        if request.user.is_authenticated():
            return HttpResponseRedirect('/')
        else:
            role = request.GET.get('user')
            return render(request, 'user/login.html', {'role': role}) 

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            cd = login_form.cleaned_data
            user_name = cd['username']
            pass_word = cd['password']
            role = cd['role']
            user  = authenticate(username=user_name, password=pass_word)
            if user is not None:
                login(request, user)
                if role == '1':
                    return HttpResponseRedirect('/userprofile')
                else:
                    return HttpResponseRedirect('/teamprofile')
            else:
                return render(request, "user/login.html", {'msg':u'用户名或密码错误', 'role': role}) 
        else:
            return HttpResponseRedirect('/')


class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect('/')

    def post(self, request):
        pass


class UserPageView(View):
    @method_decorator(login_required)
    def get(self, request):
        user = request.user
        if user.roles == 2:
            return HttpResponseRedirect('/')
        lists = EnterList.objects.filter(participant=user.username, is_checked=True)
        acts_f = []
        acts_w = []
        for list in lists:
            try:
                act = Activity.objects.get(activity_id=list.activity_id)
                if act.is_finished:
                    acts_f.append({
                        'id' : act.activity_id ,
                        'name' : act.activity_name
                    })
                else:
                    acts_w.append({
                        'id' : act.activity_id ,
                        'name' : act.activity_name                        
                    })
            except Activity.DoesNotExist:
                return render(request, 'user/userprofile.html', {
                    'acts_f': acts_f,
                    'acts_w': acts_w
                })
        return render(request, 'user/userprofile.html', {
            'acts_f': acts_f,
            'acts_w': acts_w
        })


class TeamPageView(View):
    @method_decorator(login_required)
    def get(self, request):
        user = request.user
        if user.roles == 1:
            return HttpResponseRedirect('/')
        err = ''
        if request.GET.get('err') == '1':
            err = u"填写错误，请仔细填写"
        team_id = user.team_id
        team = VTeam.objects.get(team_id=team_id)
        acts_f = Activity.objects.filter(team_id=team_id, is_finished=True).order_by('-application_time')
        acts_w = Activity.objects.filter(team_id=team_id, is_finished=False).order_by('-application_time')
        return render(request, 'user/teamprofile.html', {
            'acts_f': acts_f,
            'acts_w': acts_w,
            'team': team,
            'err': err
        })


class TeamAdminView(View):
    @method_decorator(login_required)
    def get(self, request):
        user = request.user
        if user.roles == 1:
            return HttpResponseRedirect('/')
        act_id = request.GET.get('id')
        lists = EnterList.objects.filter(activity_id=act_id)
        act = Activity.objects.get(activity_id=act_id)
        return render(request, 'user/teamactivity.html', {
            'stu_lists': lists,
            'act': act
        })

def changeStuInfo(request):
    if request.is_ajax() and request.method == 'GET':
        user = request.user
        email = request.GET.get('email')
        phone = request.GET.get('phone')
        team = request.GET.get('team')
        if email != '':
            user.email = email
        if phone != '':
            user.phone_number = phone
        user.save()
        if team != '':
            try:
                tu = TeamUser.objects.get(username=user.username, team_id = team)
            except TeamUser.DoesNotExist:
                TeamUser.objects.create(
                    username = user.username,
                    team_id = team
                )
        return HttpResponse('ok', content_type="application/text")
