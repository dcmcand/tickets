from rest_framework import generics
from django.forms.formsets import formset_factory
from django.forms.formsets import BaseFormSet
from django import forms
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.views.generic.base import TemplateView, View
from django.shortcuts import render
from django.core.urlresolvers import reverse
from .models import Transactions, Tickets, Locations, Tickets_Transactions, Report
from .serializers import TicketSerializer, TransactionSerializer
from .forms import TicketsTransactionForm, AddTicketsForm, LocationForm, get_locations, TransactionForm
import datetime
from time import strptime
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

class ApiTicketList(generics.ListCreateAPIView):
    """
    List all Tickets or Create a new Ticket
    """
    # @method_decorator(login_required)
    queryset = Tickets.objects.all()
    serializer_class = TicketSerializer


class ApiTicketAudit(generics.ListAPIView):
    """
    Shows unsold tickets
    """
    # @method_decorator(login_required)
    queryset = Tickets.objects.exclude(sold=True)
    serializer_class = TicketSerializer


class ApiTransactionList(generics.ListCreateAPIView):
    """
    List all Transactions or Create a new Transaction
    """
    # @method_decorator(login_required)
    queryset = Transactions.objects.all()
    serializer_class = TransactionSerializer


class ApiTransactionDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update, or delete a transaction instance
    """
    # @method_decorator(login_required)
    queryset = Transactions.objects.all()
    serializer_class = TransactionSerializer


class ApiTransactionReport(generics.ListAPIView):
    """
    Shows unreported transactions
    """
    # @method_decorator(login_required)
    queryset = Transactions.objects.exclude(reported=True)
    serializer_class = TransactionSerializer


class BaseTransactionFormSet(BaseFormSet):
    """
    Ensures that at least one form in the formset is filled out
    """

    def clean(self, *args, **kwargs):
        super(BaseTransactionFormSet, self).clean()
        if any(self.errors):
            return
        if not self.forms[0].has_changed():
            raise forms.ValidationError("You must enter at least one ticket number")
        ticket_numbers = []
        for form in self.forms:
            ticket_number = form.cleaned_data.get('ticket_number')
            if ticket_number in ticket_numbers:
                raise forms.ValidationError('Duplicate ticket numbers are present')
            else:
                ticket_numbers.append(ticket_number)


class AddTransaction(View):
    def get(self, request, *args, **kwargs):
        form2 = formset_factory(TicketsTransactionForm, extra=1, formset=BaseTransactionFormSet)
        form = TransactionForm
        context = {'form2': form2, 'form': form}
        return render(request, 'ticket_app/index.html', context)

    def post(self, request, *args, **kwargs):
        form = TransactionForm(request.POST)
        formset = formset_factory(TicketsTransactionForm, extra=1, formset=BaseTransactionFormSet)
        form2 = formset(request.POST)
        if form.is_valid() and form2.is_valid():
            t = form.save()
            for f in form2.forms:
                if f.has_changed():
                    trans = Transactions.objects.get(id=t.id)
                    tick = Tickets.objects.get(ticket_number=f.cleaned_data.get('ticket_number'))
                    if f.cleaned_data.get('value'):
                        tick.value = 5
                        tick.save()
                    ticket_transactions = Tickets_Transactions(ticket=tick, transactions=trans)
                    ticket_transactions.save()
            return HttpResponseRedirect("/transactions/detail/%s" % t.id)

        else:
            context = {
                'form': form,
                'form2': form2
            }
            return render(request, 'ticket_app/index.html', context)


class TicketAudit(generic.ListView):
    queryset = Tickets.objects.exclude(sold=True)
    context_object_name = "tickets"
    template_name = "ticket_app/ticket_audit.html"

    def get_context_data(self, **kwargs):
        context = super(TicketAudit, self).get_context_data(**kwargs)
        location_dict = {}
        for location in Locations.objects.all():
            location_dict[location.id] = {
                'id': location.id,
                'name': location.name,
                'tickets': Tickets.objects.filter(location=location.id).exclude(sold=True),
            }
        context['locations'] = location_dict
        return context


class AddTickets(generic.FormView):
    def get(self, request, *args, **kwargs):
        form = AddTicketsForm
        return render(request, 'ticket_app/add_tickets.html', context={'form': form})

    def post(self, request, *args, **kwargs):
        form = AddTicketsForm(request.POST)
        if form.is_valid():
            start = form.cleaned_data['start']
            end = form.cleaned_data['end']
            location = form.cleaned_data['location']

            for i in range(start, end + 1):
                t = Tickets(ticket_number=i, location=Locations.objects.get(id=location))
                t.save()

            loc = Locations.objects.get(id=location).name
            context = {'data': {'start': start, 'end': end, 'location': loc}}
            return render(request, 'ticket_app/add_tickets.html', context)
        return render(request, 'ticket_app/add_tickets.html', context={'form': form})


class TransactionsList(generic.ListView):
    model = Transactions
    context_object_name = "transactions"
    template_name = "ticket_app/view_transactions.html"
    paginate_by = 100

    def get_context_data(self, **kwargs):
        context = super(TransactionsList, self).get_context_data(**kwargs)
        context['locations'] = get_locations()
        return context


class TransactionDetail(generic.DetailView):
    model = Transactions
    context_object_name = "transaction"
    template_name = "ticket_app/transaction_detail.html"

    def get_context_data(self, **kwargs):
        context = super(TransactionDetail, self).get_context_data(**kwargs)

        context['transaction_tickets'] = Tickets_Transactions.objects.filter(transactions=context['transaction'].id)
        return context


class GenerateReport(View):
    def get(self, request, *args, **kwargs):
        context = {'form': LocationForm}
        return render(request, 'ticket_app/report.html', context)

    def post(self, request, *args, **kwargs):
        form = LocationForm(request.POST)
        if form.is_valid():
            location = form.cleaned_data['location']
            location_name = Locations.objects.get(id=location)
            report = Transactions.objects.filter(reported=False).filter(location=location).order_by('date')
            if len(report) > 0:
                r = Report(location=location_name)
                r.save()
                total = 0
                for transaction in report:
                    transaction.reported = True
                    transaction.report = r
                    transaction.save()
                    total += transaction.total()
                    transaction.tickets = []
                    tickets = Tickets_Transactions.objects.filter(transactions=transaction)
                    for ticket in tickets:
                        transaction.tickets.append(ticket.ticket.ticket_number)

                context = {'total': total, 'report': report, 'date': datetime.datetime.now(), 'location': location_name}

                return render(request, 'ticket_app/report.html', context)
            context = {'message': "There are no transactions to report"}
            return render(request, 'ticket_app/report.html', context)
        return render(request, "ticket_app/report.html", context={'form': form})


class ReportArchive(View):
    def get(self, request, *args, **kwargs):
        report = Report.objects.get(id=self.kwargs['pk'])
        location = report.location
        transactions = Transactions.objects.filter(location=location).filter(report=report)

        total = 0
        for transaction in transactions:
            total += transaction.total()
            transaction.tickets = []
            tickets = Tickets_Transactions.objects.filter(transactions=transaction)
            for ticket in tickets:
                transaction.tickets.append(ticket.ticket.ticket_number)

        context = {'total': total, 'report': transactions, 'date': report.date, 'location': report.location}

        return render(request, 'ticket_app/report.html', context)
