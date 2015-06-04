from django import forms


from .models import Tickets_Transactions

class TicketsTransactionForm(forms.ModelForm):
    class Meta:
        model = Tickets_Transactions
        fields = ['ticket', 'transactions']

class AddTicketsForm(forms.Form):

    location = forms.ChoiceField(choices=['Lebanon Library', 'Kilton Library'])
    start = forms.IntegerField(max_value=999999, min_value=99999)
    end = forms.IntegerField(max_value=999999, min_value=99999)
