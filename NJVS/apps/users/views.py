from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic.base import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from users.forms import LoginForm


class LoginView(View):
    def get(self, request):
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
                return render(request, "user/login.html", {'msg':'user or password error', 'role': role}) 
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
        userinfo = {
            'name' : user.real_name,
            'gender' : user.gender,
            'major' : user.major,
            'department' : user.department
        }
        return render(request, 'user/userprofile.html', {'user': userinfo})


class TeamPageView(View):
    @method_decorator(login_required)
    def get(self, request):
        user = request.user
        if user.roles == 1:
            return HttpResponseRedirect('/')
        return render(request, 'user/teamprofile.html',{})
        



