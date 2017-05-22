# -*- coding: utf-8 -*-
import xadmin
from xadmin import views
from xadmin.plugins.auth import UserAdmin
from django.contrib.auth.models import User
from users import models

class GlobalSetting(object):
    site_title = 'NJVS管理系统'
    site_footer = 'NJUST'
    menu_style = "accordion"

class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True

class VTeamAdmin(object):
    list_display = ('id', 'team_id', 'team_name', 'person_number', 'v_time')
    show_detail_fields = ['id']
    list_filter = ('team_id', 'team_name', 'team_property',)
    search_fields = ('team_id', 'team_name', 'team_property',)
    show_bookmarks = False
    ordering = ('v_time',)
    list_export = ['xls']
    model_icon = 'fa fa-users'

class TeamUserAdmin(object):
    list_display = ['username', 'team_id', 'team_name']
    list_export = ['xls']
    model_icon = 'fa fa-users'

xadmin.site.register(models.VTeam, VTeamAdmin)
xadmin.site.register(models.TeamUser, TeamUserAdmin)
xadmin.site.register(views.CommAdminView, GlobalSetting)
xadmin.site.register(views.BaseAdminView, BaseSetting)
