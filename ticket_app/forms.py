from django.forms import Form, ModelForm, ChoiceField, IntegerField, NumberInput, BooleanField, ValidationError
from .models import Tickets, Locations, Transactions, PaymentTypes, Tickets_Transactions


def get_locations():
    
    locations = Locations.objects.all()
    choices = []
    for l in locations:
        choices.append((l.id, l.name))
    return choices

class TicketsTransactionForm(Form):
    tickets = Tickets.objects.exclude(sold = True)
    choices = []
    for t in tickets:
        choices.append((t.ticket_number, t.ticket_number))
    ticket_number = IntegerField(max_value=999999, min_value=99999)
    value = BooleanField(label="$5 Ticket", required=False)

    def clean(self):
        cleaned_data = super(TicketsTransactionForm, self).clean()
        if self.has_changed():
            tickets = Tickets.objects.exclude(sold=True)
            in_tickets = False
            for ticket in tickets:
                #print str(ticket.ticket_number) + ' - ' + str(cleaned_data.get('ticket_number')) + " = " +  str(ticket.ticket_number == cleaned_data.get('ticket_number'))
                if ticket.ticket_number == cleaned_data.get('ticket_number'):
                    in_tickets = True
            print in_tickets
            if not in_tickets:
                self.add_error('ticket_number', 'Invalid Ticket Number')
                print self.errors


class AddTicketsForm(Form):
    location = ChoiceField(choices=get_locations())
    start = IntegerField(max_value=999999, min_value=99999)
    end = IntegerField(max_value=999999, min_value=99999)


class LocationForm(Form):
    location = ChoiceField(choices=get_locations())

class TransactionForm(ModelForm):
    class Meta:
        model = Transactions
        exclude = ['date', 'report', 'reported']
    def clean(self):
        cleaned_data = super(TransactionForm, self).clean()
        payment_type = cleaned_data.get('payment_type').type
        if payment_type:
            if payment_type == 'Check':
                if cleaned_data['check_number'] == None:
                    self.add_error('check_number', 'Check number is required when payment type is check')

