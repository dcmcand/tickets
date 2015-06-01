
from rest_framework import generics
from ticket_app.models import Transactions, Tickets
from ticket_app.serializers import TicketSerializer, TransactionSerializer

class TicketList(generics.ListCreateAPIView):
    """
    List all Tickets or Create a new Ticket
    """
    queryset = Tickets.objects.all()
    serializer_class = TicketSerializer

class TicketAudit(generics.ListAPIView):
    """
    Shows unsold tickets
    """
    queryset = Tickets.objects.exclude(sold=True)
    serializer_class = TicketSerializer


class TransactionList(generics.ListCreateAPIView):
    """
    List all Transactions or Create a new Transaction
    """
    queryset = Transactions.objects.all()
    serializer_class = TransactionSerializer

class TransactionDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update, or delete a transaction instance
    """
    queryset = Transactions.objects.all()
    serializer_class = TransactionSerializer

class TransactionReport(generics.ListAPIView):
    """
    Shows unreported transactions
    """
    queryset = Transactions.objects.exclude(reported=True)
    serializer_class = TransactionSerializer


