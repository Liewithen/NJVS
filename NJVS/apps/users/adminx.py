# -*- coding: utf-8 -*-
import xadmin
from xadmin import views
from users import models

class GlobalSetting(object):
    site_title = 'NJVS管理系统'
    site_footer = 'NJUST'


class UserAdmin(object):
    list_display = ('id', 'username', 'realname', 'team', 'phone_number', 'department', 'v_time')
    show_detail_fields = ['id']
    list_export = ('xls', )

class VTeamAdmin(object):
    list_display = ('id', 'team_id', 'team_name', 'team_property', 'person_number', 'v_time')
    show_detail_fields = ['id']
    list_export = ('xls', )

class ActivityAdmin(object):
    list_display = ('activity_id', 'team', 'application_time', 'activity_name', 'start_time', 'is_checked', 'details')
    show_detail_fields = ['details']
    list_editable = ['is_checked']
    list_export = ('xls', )

class EnterListAdmin(object):
    list_display = ('id', 'participant', 'activity', 'is_checked')
    list_editable = ['is_checked']
    list_export = ('xls', )

xadmin.site.register(models.User, UserAdmin)
xadmin.site.register(models.VTeam, VTeamAdmin)
xadmin.site.register(models.Activity, ActivityAdmin)
xadmin.site.register(models.EnterList, EnterListAdmin)
xadmin.site.register(views.CommAdminView, GlobalSetting)
