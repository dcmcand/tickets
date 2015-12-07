from django.contrib import admin

# Register your models here.
from .models import Transactions, Tickets, Tickets_Transactions, Locations,PaymentTypes, Report


class TicketsAdmin(admin.ModelAdmin):
    search_fields = ('ticket_number',)
    list_filter = ('location', 'sold')
    list_display = ('ticket_number', 'location', 'date_entered', 'date_sold', 'sold')

class TransactionsAdmin(admin.ModelAdmin):
    search_fields = ('id',)
    list_filter = ('location',)
    list_display = ('id', 'date', 'location', 'staff_initials', 'total',
                    'reported', 'report')

class Tickets_TransactionsAdmin(admin.ModelAdmin):
    search_fields = ('ticket__ticket_number',)
    

admin.site.register(Transactions, TransactionsAdmin)
admin.site.register(Tickets, TicketsAdmin)
admin.site.register(Tickets_Transactions, Tickets_TransactionsAdmin)
admin.site.register(Locations)
admin.site.register(PaymentTypes)
admin.site.register(Report)
