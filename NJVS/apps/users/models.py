# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import UserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core import validators

class VTeam(models.Model):
    team_id = models.IntegerField(verbose_name=u"账号")
    team_name = models.CharField(max_length=16, verbose_name=u"团队名称")
    team_property = models.IntegerField(verbose_name=u"团队性质")
    person_number = models.IntegerField(verbose_name=u"人数")
    v_time = models.IntegerField(verbose_name="志愿时间")


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
    v_time = models.IntegerField(verbose_name=u"志愿时间", default=0)
    team = models.ManyToManyField(VTeam, verbose_name=u"队伍", blank=True)
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
        return self.real_name

