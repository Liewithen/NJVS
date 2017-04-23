# -*- coding: utf-8 -*-
import xadmin
from xadmin import views
from activity import models

class ActivityAdmin(object):
    list_display = ('activity_id', 'application_time', 'activity_name', 'start_time', 'is_checked', 'details')
    show_detail_fields = ['details']
    list_editable = ['is_checked']
    list_export = ['xls']

class EnterListAdmin(object):
    list_display = ('id', 'participant', 'activity', 'is_checked')
    list_editable = ['is_checked']
    list_export = ['xls']

xadmin.site.register(models.Activity, ActivityAdmin)
xadmin.site.register(models.EnterList, EnterListAdmin)