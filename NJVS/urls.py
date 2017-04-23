from django.conf.urls import url
from users.views import LoginView
from verify.views import ValidateView
import xadmin
import views


urlpatterns = [
    url(r'^njvs/', xadmin.site.urls),
    url(r'^$', views.index),
    url(r'^validate/', ValidateView.as_view()),
    url(r'^login/$', LoginView.as_view())
]
