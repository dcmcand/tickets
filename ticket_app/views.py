from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from ticket_app.models import Transactions, Tickets, Locations, PaymentTypes
from ticket_app.serializers import TicketSerializer, TransactionSerializer

# Create your views here.
@api_view(['GET', 'POST'])
def ticket_list(request, format=None):
    """
    List all tickets or create a new ticket
    :param request:
    :return:
    """
    if request.method == 'GET':
        tickets = Tickets.objects.all()
        serializer = TicketSerializer(tickets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = TicketSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

