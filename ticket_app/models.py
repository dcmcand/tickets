from django.db import models
from datetime import datetime
# Create your models here.
from django.db import models

class PaymentTypes(models.Model):
    class Meta:
        verbose_name_plural = "Payment Types"
    type = models.CharField(max_length=255, unique=True)

    def __unicode__(self):
        return self.type

class Locations(models.Model):
    class Meta:
        verbose_name_plural = "Locations"

    name = models.CharField(max_length=255, unique=True)

    def __unicode__(self):
        return self.name

class Tickets(models.Model):
    class Meta:
        verbose_name_plural = "Tickets"
    value = models.PositiveIntegerField(default=10)
    ticket_number = models.PositiveIntegerField(unique=True)
    date_entered = models.DateField(auto_now_add=True)
    sold = models.BooleanField(default=False)
    date_sold = models.DateField(blank=True, null=True)
    location = models.ForeignKey(Locations)
    def __unicode__(self):
        return str(self.ticket_number)

class Transactions(models.Model):
    class Meta:
        verbose_name_plural = "Transactions"
        ordering = ["-date"]

    date = models.DateField(auto_now_add=True)
    location = models.ForeignKey(Locations)
    payment_type = models.ForeignKey(PaymentTypes)
    check_number = models.PositiveIntegerField(null=True, blank=True)
    reported = models.BooleanField(default=False)
    staff_initials = models.CharField(max_length=4)
    report = models.ForeignKey('Report', blank=True, null=True)
    def total(self):
        tickets = Tickets_Transactions.objects.filter(transactions=self.id)
        total = 0
        for ticket in tickets:
            total += ticket.ticket.value
        return total


    def __unicode__(self):
        return str(str(self.id) + " - " + str(self.date) + ' - $' + str(self.total()))

class Tickets_Transactions(models.Model):
    class Meta:
        verbose_name_plural = "Tickets and Transactions"
    ticket = models.OneToOneField(Tickets, unique=True)
    transactions = models.ForeignKey(Transactions)
    def save(self, *args, **kwargs):
        super(Tickets_Transactions, self).save(*args, **kwargs)
        ticket = self.ticket
        ticket.sold=True
        ticket.date_sold = datetime.now()
        ticket.save()
    def __unicode__(self):
        return 'ticket number:' + str(self.ticket.ticket_number) + ', Transaction: ' + str(self.transactions.id)

class Report(models.Model):
    location = models.ForeignKey('Locations')
    date = models.DateField(auto_now_add=True)

    def __unicode__(self):
        return str(self.location) + "-" + str(self.date)


