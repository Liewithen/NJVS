# encoding: utf-8
from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from verify.forms import ValidateForm
from verify.tasks import validate_User
from .models import UserValidate
# Create your views here.


class ValidateView(View):
    # @method_decorator(login_required)
    def get(self, request):
        if request.is_ajax():
            validate = ValidateForm(request.GET)
            if validate.is_valid():
                cd = validate.cleaned_data;
                username = cd['username']
                jwc_pwd = cd['jwc_pwd']
                validate_User.delay(username, jwc_pwd)
                data = "submitting"
                return HttpResponse(data, content_type="application/text") 
        else:
            return render(request, 'user/validate.html')


def checkResult(request):
    if request.method == 'GET':
        username = request.GET.get('username')
        try:
            u = UserValidate.objects.get(username=username)
            state = u.validate
        except UserValidate.DoesNotExist:
            state = '0'
        return HttpResponse(state, content_type="application/text")




