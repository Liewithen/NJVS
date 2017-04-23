from django import forms

class ValidateForm(forms.Form):
    username = forms.CharField(required=True, max_length=12)
    jwc_pwd = forms.CharField(required=True)
