from django.conf.urls import include, url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from TaskApp import views

urlpatterns = [
    url(r'^task/(?P<id>[0-9]+)/$', views.TaskList.as_view()),
    url(r'^task/',views.TaskList.as_view()),
    url(r'^admin/', admin.site.urls),
]

urlpatterns = format_suffix_patterns(urlpatterns)