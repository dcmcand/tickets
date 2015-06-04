from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = {

    url(r'^tickets/audit/(?P<location>[0-9]{1})/?$', views.TicketAudit.as_view()),
    url(r'^api/tickets/?$', views.TicketList.as_view()),
    url(r'^api/transactions/report/?$', views.TransactionReport.as_view()),
    url(r'^api/transactions/(?P<pk>[0-9]+)/?$', views.TransactionDetail.as_view()),
    url(r'^api/transactions/?$', views.TransactionList.as_view()),
    url(r'^', views.TransactionForm.as_view()),
}

urlpatterns = format_suffix_patterns(urlpatterns)
