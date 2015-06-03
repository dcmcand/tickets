from django.forms import Form


from .models import Tickets_Transactions

class TicketsTransactionForm(Form):
    class Meta:
        model = Tickets_Transactions
        fields = ['ticket', 'transactions']

