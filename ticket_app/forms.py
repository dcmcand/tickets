from django import forms
from .models import Tickets_Transactions, Locations


class TicketsTransactionForm(forms.ModelForm):
    class Meta:
        model = Tickets_Transactions
        fields = ['ticket', 'transactions']


class AddTicketsForm(forms.Form):
    locations = (
        ('Leb','Lebanon'),
        ('KPL','Kilton')
    )
    # locations = Locations.objects.all()
    # for l in locations:
    #     form_choices.append(l.name)
    location = forms.ChoiceField(choices=locations)
    start = forms.IntegerField(max_value=999999, min_value=99999)
    end = forms.IntegerField(max_value=999999, min_value=99999)
