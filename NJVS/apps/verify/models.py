# -*- coding: utf-8 -*-
from django.db import models

class UserValidate(models.Model):
    username = models.CharField(max_length=12, verbose_name=u"学号")
    validate = models.IntegerField(choices=((0,u"验证中"),(1,u"验证成功"),(2,u"验证失败")), verbose_name=u"验证状态")

    class Meta:
        verbose_name = u"验证状态"
        verbose_name_plural = verbose_name
