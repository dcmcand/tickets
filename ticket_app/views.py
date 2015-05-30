from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from ticket_app.models import Transactions, Tickets, Locations, PaymentTypes
from

# Create your views here.


