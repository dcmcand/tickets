from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = {

    # url(r'^tickets/audit/?$', views.TicketAudit),
    url(r'^tickets/audit/?$', views.TicketAudit.as_view()),
    url(r'^tickets/?$', views.AddTickets.as_view()),
    url(r'^api/tickets/?$', views.ApiTicketList.as_view()),
    url(r'^api/transactions/report/?$', views.ApiTransactionReport.as_view()),
    url(r'^api/transactions/(?P<pk>[0-9]+)/?$', views.ApiTransactionDetail.as_view()),
    url(r'^api/transactions/?$', views.ApiTransactionList.as_view()),
    url(r'^', views.TransactionForm.as_view()),
}
