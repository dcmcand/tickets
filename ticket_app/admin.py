from django.contrib import admin

# Register your models here.
from .models import Transactions, Tickets, Tickets_Transactions, Locations,PaymentTypes, Report

admin.site.register(Transactions)
admin.site.register(Tickets)
admin.site.register(Tickets_Transactions)
admin.site.register(Locations)
admin.site.register(PaymentTypes)
admin.site.register(Report)
