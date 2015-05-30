from django.forms import widgets
from rest_framework import serializers
from ticket_app.models import Transactions, Tickets, Locations, PaymentTypes

location_choices = []

for l in Locations.objects.all():
    location_choices.append(l.name)

payment_types = []

for p in PaymentTypes.objects.all():
    payment_types.append(p.type)

class TicketsSerializer(serializers.Serializer):
    ticket_number = serializers.IntegerField(required=True)
    date_entered = serializers.DateField(read_only=True)
    sold = serializers.BooleanField(default = False)
    location = serializers.ChoiceField(choices=location_choices, default='Lebanon Library')

    def create(self):
        return Tickets.object.create(**validated_data)

    def update(self):
        instance.ticket_number = validated_data.get('ticket_number', instance.ticket_number)
        instance.sold = validated_data.get('sold', instance.sold)
        instance.location = validated_data.get('location', instance.location)

class TransactionsSerializer(serializers.Serializer):
    tickets = []
    for t in Tickets.objects.exclude(sold=True):
        tickets.append(t.ticket_number)
    ticket_number = serializers.IntegerField(choices=tickets, required = True)
    date = serializers.DateField(auto_now_add = True)
    location = serializers.ChoiceField(choices = location_choices, default='Leb')
    check_number = serializers.IntegerField(required=False, allow_blank=True)
    reported = serializers.BooleanField(default=False)

    def create(self):
        return Transactions.object.create(**validated_data)

    def update(self):
        pass


