
from rest_framework import generics
from django.utils.decorators import method_decorator
from django.forms.formsets import formset_factory
from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic
from django.views.generic.base import TemplateView, View
from .models import Transactions, Tickets
from .serializers import TicketSerializer, TransactionSerializer
from .forms import TicketsTransactionForm, AddTicketsForm

class ApiTicketList(generics.ListCreateAPIView):
    """
    List all Tickets or Create a new Ticket
    """
    #@method_decorator(login_required)
    queryset = Tickets.objects.all()
    serializer_class = TicketSerializer

class ApiTicketAudit(generics.ListAPIView):
    """
    Shows unsold tickets
    """
    #@method_decorator(login_required)
    queryset = Tickets.objects.exclude(sold=True)
    serializer_class = TicketSerializer


class ApiTransactionList(generics.ListCreateAPIView):
    """
    List all Transactions or Create a new Transaction
    """
    #@method_decorator(login_required)
    queryset = Transactions.objects.all()
    serializer_class = TransactionSerializer

class ApiTransactionDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update, or delete a transaction instance
    """
    #@method_decorator(login_required)
    queryset = Transactions.objects.all()
    serializer_class = TransactionSerializer

class ApiTransactionReport(generics.ListAPIView):
    """
    Shows unreported transactions
    """
    #@method_decorator(login_required)
    queryset = Transactions.objects.exclude(reported=True)
    serializer_class = TransactionSerializer

class TransactionForm(generic.FormView):
    template_name = 'ticket_app/index.html'
    #form_class = TicketsTransactionForm
    transactionformset = formset_factory(TicketsTransactionForm)
    form_class = transactionformset
    success_url = '/success/'

class TicketAudit(generic.ListView):
    queryset = Tickets.objects.exclude(sold=True)
    context_object_name = "tickets"
    template_name = "ticket_app/ticket_audit.html"
    def get_context_data(self, **kwargs):
        context = super(TicketAudit, self).get_context_data(**kwargs)
        context['leb_tickets'] = Tickets.objects.exclude(sold=True).filter(location=1).order_by('ticket_number')
        context['kpl_tickets'] = Tickets.objects.exclude(sold=True).filter(location=2).order_by('ticket_number')
        return context

class AddTickets(generic.FormView):
    form_class = AddTicketsForm
    template_name = "ticket_app/add_tickets.html"
    success_url = '/success/'

class ViewTransactions(TemplateView):
    template_name = 'ticket_app/view_transactions.html'

class GenerateReport(TemplateView):
    template_name = 'ticket_app/report.html'

class Success(View):
    def get(self):
        return HttpResponse('Success')



