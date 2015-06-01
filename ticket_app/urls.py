from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = {
    url(r'^tickets/audit/?$', views.TicketAudit.as_view()),
    url(r'^tickets/?$', views.TicketList.as_view()),
    url(r'^transactions/report/?$', views.TransactionReport.as_view()),
    url(r'^transactions/(?P<pk>[0-9]+)/?$', views.TransactionDetail.as_view()),
    url(r'^transactions/?$', views.TransactionList.as_view()),
}

urlpatterns = format_suffix_patterns(urlpatterns)