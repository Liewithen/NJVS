from django.conf.urls import url
from users.views import LoginView, LogoutView, UserPageView, TeamPageView, TeamAdminView
from verify.views import ValidateView, checkResult
from news.views import NewsView
from activity.views import ActivityView, ActProfileView, joinActivity
from django.views.static import serve
from NJVS.settings import MEDIA_ROOT
from django.conf.urls import include
import DjangoUeditor
import xadmin
import views

# user
urlpatterns = [
    url(r'^njvs/', xadmin.site.urls),
    url(r'^$', views.index),
    url(r'^login/$', LoginView.as_view()),
    url(r'^logout/$', LogoutView.as_view()),
    url(r'^userprofile/', UserPageView.as_view()),
    url(r'^teamprofile/', TeamPageView.as_view()),
    url(r'^actadmin/', TeamAdminView.as_view()),
    url(r'^media/(?P<path>.*)/$', serve, {"document_root": MEDIA_ROOT}),
    url(r'^ueditor/', include('DjangoUeditor.urls')),
]

#verify
urlpatterns += [
    url(r'^validate/', ValidateView.as_view()),
    url(r'^check/', checkResult)
]

# news
urlpatterns += [
    url(r'^news/', NewsView.as_view()),
]

# activity
urlpatterns += [
    url(r'^activity/', ActivityView.as_view()),
    url(r'^actprofile/', ActProfileView.as_view()),
    url(r'^join/', joinActivity)
]

