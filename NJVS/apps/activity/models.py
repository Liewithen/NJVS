# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from datetime import datetime

from django.db import models

class Activity(models.Model):
    activity_id = models.AutoField(primary_key=True, verbose_name=u"活动ID")
    application_time = models.DateTimeField(auto_now=True, verbose_name=u"申请时间")
    activity_name = models.CharField(max_length=30, verbose_name=u"活动名称")
    team_name = models.CharField(max_length=100, verbose_name=u"团队名称", default="")
    start_time = models.DateTimeField(verbose_name=u"开始时间") 
    end_time = models.DateTimeField(verbose_name=u"结束时间")
    per_time = models.IntegerField(verbose_name=u"每日时间", default=0)
    join_number = models.IntegerField(verbose_name=u"参与人数", default=0)
    need_number = models.IntegerField(verbose_name=u"人数", default=0)
    is_checked = models.BooleanField(verbose_name=u"审核状态", default=False)
    is_finished = models.BooleanField(verbose_name=u"完成状态", default=False)
    details = models.TextField(verbose_name=u"详情")

    class Meta:
        db_table = 'njvs_activity'
        verbose_name = u"活动列表"
        verbose_name_plural = u"活动列表"
    
    def __unicode__(self):
        return self.activity_name

class EnterList(models.Model):
    participant = models.CharField(max_length=16, verbose_name=u"参与者")
    activity = models.CharField(max_length=30, verbose_name=u"活动名称")
    is_checked = models.BooleanField(verbose_name=u"审核状态")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"申报时间")

    class Meta:
        db_table = 'njvs_enterlist'
        verbose_name = u"报名列表"
        verbose_name_plural = u"报名列表"
    
    def __unicode__(self):
        return self.participant

