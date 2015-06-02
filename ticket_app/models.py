from django.db import models

# Create your models here.
from django.db import models

class PaymentTypes(models.Model):
    type = models.CharField(max_length=255, unique=True)

    def __unicode__(self):
        return self.type

class Locations(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __unicode__(self):
        return self.name

class Tickets(models.Model):
    ticket_number = models.PositiveIntegerField(unique=True)
    date_entered = models.DateField(auto_now_add=True)
    sold = models.BooleanField(default=False)
    location = models.ForeignKey(Locations, to_field="name")
    def __unicode__(self):
        return str(self.ticket_number)

class Transactions(models.Model):
    date = models.DateField(auto_now_add=True)
    location = models.ForeignKey(Locations, to_field="name")
    payment_type = models.ForeignKey(PaymentTypes)
    check_number = models.PositiveIntegerField(null=True)
    reported = models.BooleanField(default=False)
    staff_initials = models.CharField(max_length=4)
    total = models.IntegerField()

    def __unicode__(self):
        return str(self.id)

class Tickets_Transactions(models.Model):
    ticket = models.ForeignKey(Tickets)
    transactions = models.ForeignKey(Transactions)



