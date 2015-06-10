from django.forms import Form, ModelForm, ChoiceField, IntegerField, NumberInput
from .models import Tickets, Locations, Transactions


def get_locations():
    
    locations = Locations.objects.all()
    choices = []
    for l in locations:
        choices.append((l.id, l.name))
    return choices


class TicketsTransactionForm(Form):
    tickets = Tickets.objects.exclude(sold=True)
    choices = []
    for t in tickets:
        choices.append((t.id, t.ticket_number))
    ticket_number = ChoiceField(choices=choices, widget=NumberInput)



class AddTicketsForm(Form):
    location = ChoiceField(choices=get_locations())
    start = IntegerField(max_value=999999, min_value=99999)
    end = IntegerField(max_value=999999, min_value=99999)


class LocationForm(Form):
    location = ChoiceField(choices=get_locations())

class TransactionForm(ModelForm):
    class Meta:
        model = Transactions
        fields = ['location']