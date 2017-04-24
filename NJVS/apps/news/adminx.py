# -*- coding: utf-8 -*-
import xadmin
from xadmin import views
from news import models

class BannerAdmin(object):
    list_display = ('id', 'title', 'image', 'url', 'index', 'add_time')
    show_detail_fields = ['id']
    list_export = ['xls']       

class NewsAdmin(object):
    list_display = ('id', 'title', 'add_time')
    show_detail_fields = ['id']
    list_export = ['xls'] 
    style_fields = {"detail" : "ueditor"}  

xadmin.site.register(models.Banner, BannerAdmin)
xadmin.site.register(models.News, NewsAdmin)    