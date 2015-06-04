from django import forms
from .models import Locations


from .models import Tickets_Transactions

class TicketsTransactionForm(forms.ModelForm):
    class Meta:
        model = Tickets_Transactions
        fields = ['ticket', 'transactions']

class AddTicketsForm(forms.Form):
    locations = Locations.objects.all()
    location_choices=[]
    for l in locations:
        location_choices.append(l.name)
    location = forms.ChoiceField(choices=location_choices)
    start = forms.IntegerField(max_value=999999, min_value=99999)
    end = forms.IntegerField(max_value=999999, min_value=99999)
