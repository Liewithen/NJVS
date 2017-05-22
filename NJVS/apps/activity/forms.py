# encoding: utf-8
from django import forms
from .models import Activity

class ApplyActForm(forms.ModelForm):
    start_time = forms.CharField(required=True)
    end_time = forms.CharField(required=True)
    class Meta:
        model = Activity
        fields = ['activity_name', 'contact_qq', 'contact_phone', 'place', 'time_detail', 'per_time', 'days', 'weeks', 'need_number', 'details']
