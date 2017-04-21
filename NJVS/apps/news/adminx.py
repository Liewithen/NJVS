# -*- coding: utf-8 -*-
import xadmin
from xadmin import views
from news import models

class BannerAdmin(object):
    list_display = ('id', 'title', 'image', 'url', 'index', 'add_time')
    show_detail_fields = ['id']
    list_export = ['xls']       

class NewsAdmin(object):
    list_display = ('id', 'title', 'image', 'add_time', 'detail')
    show_detail_fields = ['id']
    list_export = ['xls'] 

xadmin.site.register(models.Banner, BannerAdmin)
xadmin.site.register(models.News, NewsAdmin)    