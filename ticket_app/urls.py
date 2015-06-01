from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = {
    url(r'^tickets/$', views.ticket_list),
}

urlpatterns = format_suffix_patterns(urlpatterns)