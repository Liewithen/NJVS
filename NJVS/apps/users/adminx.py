# -*- coding: utf-8 -*-
import xadmin
from xadmin import views
from users import models

class GlobalSetting(object):
    site_title = 'NJVS管理系统'
    site_footer = 'NJUST'
    menu_style = "accordion"

class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True
  

class UserAdmin(object):
    list_display = ('id', 'roles', 'username', 'real_name', 'gender', 'team', 'phone_number', 'department', 'v_time')
    search_fields = ['username', 'real_name']
    list_filter = ['roles', 'username', 'real_name', 'team', 'department']
    show_detail_fields = ['id']
    list_export = ['xls']

class VTeamAdmin(object):
    list_display = ('id', 'team_id', 'team_name', 'team_property', 'person_number', 'v_time')
    show_detail_fields = ['id']
    list_export = ['xls']


xadmin.site.register(models.User, UserAdmin)
xadmin.site.register(models.VTeam, VTeamAdmin)
xadmin.site.register(views.CommAdminView, GlobalSetting)
xadmin.site.register(views.BaseAdminView, BaseSetting)
