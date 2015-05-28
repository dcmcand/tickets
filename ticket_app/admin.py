from django.contrib import admin

# Register your models here.
from .models import Transactions, Tickets

admin.site.register(Transactions)
admin.site.register(Tickets)
