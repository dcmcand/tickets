from django.forms import widgets
from rest_framework import serializers
from ticket_app.models import Transactions, Tickets, Locations, PaymentTypes

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tickets
        fields = ('ticket_number', 'date_entered', 'sold', 'location', 'date_sold')

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transactions
        fields = ('date', 'location','payment_type', 'staff_initials', 'check_number', 'reported', 'total')




