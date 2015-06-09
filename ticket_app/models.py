from django.db import models
from datetime import datetime
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
    date_sold = models.DateField(blank=True, null=True)
    location = models.ForeignKey(Locations)
    def __unicode__(self):
        return str(self.ticket_number)

class Transactions(models.Model):
    date = models.DateField(auto_now_add=True)
    location = models.ForeignKey(Locations)
    payment_type = models.ForeignKey(PaymentTypes)
    check_number = models.PositiveIntegerField(null=True, blank=True)
    reported = models.BooleanField(default=False)
    staff_initials = models.CharField(max_length=4)
    def total(self):
        tickets = Tickets_Transactions.objects.filter(transactions=self.id).count()
        total = tickets * 10
        return total
    date_reported = models.DateField(blank=True, null=True)

    def __unicode__(self):
        return str(self.id)

class Tickets_Transactions(models.Model):
    ticket = models.OneToOneField(Tickets, unique=True)
    transactions = models.ForeignKey(Transactions)
    def save(self, *args, **kwargs):
        super(Tickets_Transactions, self).save(*args, **kwargs)
        ticket = self.ticket
        ticket.sold=True
        ticket.date_sold = datetime.now()
        ticket.save()



