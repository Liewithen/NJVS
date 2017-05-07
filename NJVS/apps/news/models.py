# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from datetime import datetime
from DjangoUeditor.models import UEditorField


class Banner(models.Model):
    title = models.CharField(max_length=100, verbose_name=u"新闻题目")
    image = models.ImageField(max_length=100, upload_to="banner/%Y/%m", verbose_name=u"图片")
    url = models.URLField(max_length=200, verbose_name=u"访问地址")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"轮播图"
        verbose_name_plural = verbose_name
    
    def __unicode__(self):
        return self.title

class News(models.Model):
    title = models.CharField(max_length=100, verbose_name=u"新闻标题")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")
    detail = UEditorField(verbose_name=u'新闻详情',width=850, height=300, imagePath="news/ueditor/", 
    filePath="news/ueditor", default='')
    
    class Meta:
        verbose_name = u"新闻"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.title
