from django.db import models

# Create your models here.
from django.db import models


class Transactions(models.Model):
    ticket_number = models.ForeignKey('Tickets', to_field="ticket_number")
    date = models.DateField(auto_now_add=True)
    library_choices = (
        ('Leb', "Lebanon"),
        ('KPL', "Kilton"),
    )
    library = models.CharField(max_length=3, choices=library_choices)
    payment_type_choices = (
        ('cash', 'Cash'),
        ('check', 'Check'),
    )
    payment_type = models.CharField(max_length=5, choices = payment_type_choices, default = "cash")
    check_number = models.PositiveIntegerField(null=True)
    reported = models.BooleanField(default=False)
    staff_initials = models.CharField(max_length=4)

    def __unicode__(self):
        return str(self.id)


class Tickets(models.Model):
    ticket_number = models.PositiveIntegerField(unique=True)
    date_entered = models.DateField(auto_now_add=True)
    sold = models.BooleanField(default=False)

    def __unicode__(self):
        return str(self.ticket_number)
