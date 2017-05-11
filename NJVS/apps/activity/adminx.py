# -*- coding: utf-8 -*-
import xadmin
from xadmin import views
from activity import models

class ActivityAdmin(object):
    list_display = ('activity_id', 'application_time', 'activity_name', 'team_name', 'start_time', 'end_time', 'per_time', 'is_checked', 'details', 'is_finished')
    show_detail_fields = ['details']
    list_editable = ['is_checked', 'is_finished']
    list_filter = ('application_time', 'activity_name', 'team_name','is_checked', 'is_finished')
    search_fields = ('application_time', 'activity_name', 'team_name','is_checked', 'is_finished')
    list_export = ['xls']
    model_icon = 'fa fa-users'
    show_bookmarks = False
    refresh_times = [3, 5]

class EnterListAdmin(object):
    list_display = ('id', 'participant', 'activity', 'is_checked')
    list_editable = ['is_checked']
    list_export = ['xls']
    show_bookmarks = False
    refresh_times = [3, 5]

xadmin.site.register(models.Activity, ActivityAdmin)
xadmin.site.register(models.EnterList, EnterListAdmin)