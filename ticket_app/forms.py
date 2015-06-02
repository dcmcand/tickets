from django.forms import ModelForm


from .models import Transactions

class TransactionForm(ModelForm):
    class Meta:
        model = Transactions
        fields = ['location', 'payment_type', 'check_number', 'staff_initials']

