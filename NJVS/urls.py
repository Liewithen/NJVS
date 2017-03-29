# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.contrib import admin

import xadmin                        # 覆盖admin配置
xadmin.autodiscover()
from xadmin.plugins import xversion  # version模块自动注册需要版本控制的 Model
xversion.register_models()

import views

urlpatterns = [
    url(r'^njvs/', xadmin.site.urls),
    url(r'^$', views.index)
]
