from django import forms
from .models import Tickets_Transactions, Locations


def get_locations():
    
    locations = Locations.objects.all()
    choices = []
    for l in locations:
        choices.append((l.id, l.name))
    return choices
class TicketsTransactionForm(forms.Form):
    pass

class AddTicketsForm(forms.Form):
    location = forms.ChoiceField(choices=get_locations())
    start = forms.IntegerField(max_value=999999, min_value=99999)
    end = forms.IntegerField(max_value=999999, min_value=99999)


class LocationForm(forms.Form):
    location = forms.ChoiceField(choices=get_locations())
