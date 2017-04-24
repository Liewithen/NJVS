from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from verify.forms import ValidateForm
from verify.tasks import validate_User
# Create your views here.


class ValidateView(View):
    @method_decorator(login_required)
    def get(self, request):
        return render(request, 'validate.html')
    
    @method_decorator(login_required)
    def post(self, request):
        validate = ValidateForm(request.POST)
        if validate.is_valid():
            cd = validate.cleaned_data;
            username = cd['username']
            jwc_pwd = cd['jwc_pwd']
            validate_User.delay(username, jwc_pwd)
            return render(request, 'validate.html')
        else:
            return render(request, 'validate.html', {'msg':'error'})

