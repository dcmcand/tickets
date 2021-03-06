from django.conf.urls import url, include
from . import views


#api_urls = [
#    url(r'^transactions/report/?$', views.ApiTransactionReport.as_view()),
#    url(r'^transactions/(?P<pk>[0-9]+)/?$', views.ApiTransactionDetail.as_view()),
#    url(r'^transactions/?$', views.ApiTransactionList.as_view()),
#    url(r'^tickets/?$', views.ApiTicketList.as_view()),
#]


tickets_urls = [
    url(r'^audit/?$', views.TicketAudit.as_view()),
    url(r'^$', views.AddTickets.as_view()),
    #url(r'^/?$', views.AddTickets.as_view()),
]


transactions_urls = [
    #url(r'^/?$', views.TransactionsList.as_view(), name="Transactions List"),
    url(r'^$', views.TransactionsList.as_view(), name="Transactions List"),
     url(r'^detail/?$', views.TransactionDetail, name="Transaction Detail"),
    url(r'^detail/(?P<pk>\d+)/?$', views.TransactionDetail.as_view(), name="Transaction Detail"),

]


urlpatterns = [
    url(r'^report/(?P<pk>\d+)/?$', views.ReportArchive.as_view(), name='Report Archive'),
    #url(r'^report/(?P<pk>[0-9])/?$', views.ReportArchive.as_view(), name='Report Archive'),
    url(r'^report/?$', views.GenerateReport.as_view()),
    url(r'^tickets/', include(tickets_urls)),
    #url(r'^api/', include(api_urls)),
    url(r'^transactions/', include(transactions_urls)),
    url(r'^$', views.AddTransaction.as_view()),
    #url(r'^/?$', views.AddTransaction.as_view()),
]
