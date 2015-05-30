from django.forms import widgets
from rest_framework import serializers
from ticket_app.models import Transactions, Tickets, Locations, PaymentTypes

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tickets
        fields = ('ticket_number', 'date_entered', 'sold', 'location')

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transactions
        fields = ('ticket_number', 'date', 'location', 'check_number', 'reported')




