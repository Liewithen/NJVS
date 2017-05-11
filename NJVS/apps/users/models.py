# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import UserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core import validators

class VTeam(models.Model):
    team_id = models.IntegerField(verbose_name=u"账号")
    team_name = models.CharField(max_length=16, verbose_name=u"团队名称")
    image = models.ImageField(max_length=100, upload_to="team/%Y/%m", verbose_name=u"图片", blank=True)
    team_property = models.IntegerField(verbose_name=u"团队性质")
    details = models.TextField(verbose_name=u"团队详情", blank=True, default="")
    leader_id = models.CharField(verbose_name=u"负责人账号", max_length=16, unique=True,)
    person_number = models.IntegerField(verbose_name=u"人数")
    v_time = models.IntegerField(verbose_name="志愿总时间")


    class Meta:
        db_table = 'njvs_team'
        verbose_name = u"团队信息"
        verbose_name_plural = u"团队信息"
    
    def __unicode__(self):
        return self.team_name


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=16, unique=True, verbose_name=u"学号")
    real_name = models.CharField(max_length=30, null=True, verbose_name=u"姓名", blank=True)
    gender = models.CharField(max_length=6, choices=(("male", u"男"),("female", u"女")), verbose_name=u"性别", default="male")
    major = models.CharField(max_length=30, verbose_name=u"专业", default="", blank=True)
    department = models.CharField(max_length=30, verbose_name=u"院系", default="", blank=True)
    birthday = models.CharField(max_length=8,verbose_name=u"出生日期",blank=True, default="")
    political = models.CharField(max_length=30,verbose_name=u"政治面貌",blank=True, default="")
    idcard = models.CharField(max_length=30,verbose_name=u"身份证号",blank=True, default="")
    v_time = models.IntegerField(verbose_name=u"志愿时间", default=0)
    phone_number = models.CharField(max_length=11, verbose_name=u"手机号", blank=True)
    roles = models.IntegerField(choices=((0, u"管理员"),(1, u"学生"),(2, u"团队")), verbose_name=u"身份", default=1)
    email = models.EmailField(blank=True)

    is_active = models.BooleanField(default=True, verbose_name=u"激活状态")
    is_staff = models.BooleanField(default=False, verbose_name=u"管理员状态")

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
    objects = UserManager()

    class Meta:
        db_table = 'njvs_users'
        verbose_name = u"学生信息"
        verbose_name_plural = u"学生信息"
    
    def __unicode__(self):
        return self.username


class TeamUser(models.Model):
    username = models.CharField(max_length=16, unique=True, verbose_name=u"学号")
    team_id = models.IntegerField(verbose_name=u"团队账号")
    team_name = models.CharField(max_length=100, verbose_name=u"团队名", default="")

    class Meta:
        verbose_name = u"学生-团队信息"
        verbose_name_plural = verbose_name
    
    def __unicode__(self):
        return u'%s_%s' % (self.team_id, self.username)
