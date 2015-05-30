from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from ticket_app.models import Transactions, Tickets, Locations, PaymentTypes
from ticket_app.serializers import TicketSerializer, TransactionSerializer

# Create your views here.
class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

@csrf_exempt
def ticket_list(request):
    """
    List all landfill tickets or add landfill tickets
    :param request:
    :return:
    """
    if request.method == 'GET':
        tickets = Tickets.objects.all()
        serializer = TicketSerializer(tickets, many=True)
        return JSONResponse(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = TicketSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)
