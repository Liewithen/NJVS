from django.conf.urls import url
from users.views import LoginView
from verify.views import ValidateView
from django.views.static import serve
from NJVS.settings import MEDIA_ROOT
from django.conf.urls import include
import DjangoUeditor
import xadmin
import views


urlpatterns = [
    url(r'^njvs/', xadmin.site.urls),
    url(r'^$', views.index),
    url(r'^validate/', ValidateView.as_view()),
    url(r'^login/$', LoginView.as_view()),
    url(r'^media/(?P<path>.*)/$', serve, {"document_root": MEDIA_ROOT}),
    url(r'^ueditor/',include('DjangoUeditor.urls' )),
]


