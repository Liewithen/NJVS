# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import UserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core import validators

class VTeam(AbstractBaseUser):
    team_id = models.IntegerField(verbose_name=u"账号")
    team_name = models.CharField(max_length=16, verbose_name=u"团队名称")
    team_property = models.IntegerField(verbose_name=u"团队性质")
    person_number = models.IntegerField(verbose_name=u"人数")
    v_time = models.IntegerField(verbose_name="志愿时间")
    USERNAME_FIELD = 'team_name'

    class Meta:
        db_table = 'njvs_team'
        verbose_name = u"团队信息"
        verbose_name_plural = u"团队信息"


class User(AbstractBaseUser):
    username = models.CharField(max_length=16, unique=True, verbose_name=u"学号")
    realname = models.CharField(max_length=30, null=True, verbose_name=u"姓名")
    phone_number = models.CharField(max_length=11, verbose_name=u"手机号")
    department = models.CharField(max_length=30, verbose_name=u"院系")
    v_time = models.IntegerField(verbose_name=u"志愿时间")
    team = models.ManyToManyField(VTeam, verbose_name=u"队伍", blank=True)
    USERNAME_FIELD = 'username'

    class Meta:
        db_table = 'njvs_users'
        verbose_name = u"学生信息"
        verbose_name_plural = u"学生信息"


class Activity(models.Model):
    activity_id = models.AutoField(primary_key=True, verbose_name=u"活动ID")
    team = models.ManyToManyField(VTeam, verbose_name=u"参与队伍")
    application_time = models.DateField(auto_now=True, verbose_name=u"申请时间")
    activity_name = models.CharField(max_length=30, verbose_name=u"活动名称")
    start_time = models.DateTimeField(verbose_name=u"开始时间") 
    end_time = models.DateTimeField(verbose_name=u"结束时间")
    person_number = models.IntegerField(verbose_name=u"参与人数")
    is_checked = models.BooleanField(verbose_name=u"审核状态")
    details = models.TextField(verbose_name=u"详情")

    class Meta:
        db_table = 'njvs_activity'
        verbose_name = u"活动列表"
        verbose_name_plural = u"活动列表"

class EnterList(models.Model):
    participant = models.CharField(max_length=16, verbose_name=u"参与者")
    activity = models.CharField(max_length=30, verbose_name=u"活动名称")
    is_checked = models.BooleanField(verbose_name=u"审核状态")

    class Meta:
        db_table = 'njvs_enterlist'
        verbose_name = u"报名列表"
        verbose_name_plural = u"报名列表"
