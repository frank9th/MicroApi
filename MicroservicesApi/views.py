from django.shortcuts import render
import pymongo
import json
import requests
from rest_framework import viewsets 
from .models import AdministrativeBudget, MDABudget, EconomicRevenue, EconomicExpenditure, GovernmentFunctions, DailyBudget
from .serializers import AdministrativeSerializer, MDABudgetSerializer, EconomicRevenueSerializer, EconomicExpenditureSerializer, GovernmentFunctionsSerializer, DailyBudgetSerializer 
from rest_framework.decorators import action


# Create your views here.

def home(request):
	return render(request, 'home.html')


class AdministrativeView(viewsets.ModelViewSet):
    queryset = AdministrativeBudget.objects.all()  # this code is to call all object from the db
    serializer_class = AdministrativeSerializer  # this code use the class defined in the serializers.py

'''
added a C.B view for returning a list of all MDA transactions available in the database
assumed a serializer of name MDABudgetSerializer has already been made.
'''
class MDABudgetView(viewsets.ModelViewSet):
    queryset = MDABudget.objects.all()
    serializer_class = MDABudgetSerializer


class EconomicRevenueView(viewsets.ModelViewSet):
    queryset = EconomicRevenue.objects.all()
    serializer_class = EconomicRevenueSerializer

class EconomicExpenditureView(viewsets.ModelViewSet):
    queryset = EconomicExpenditure.objects.all()
    serializer_class = EconomicExpenditureSerializer

class GovernmentFunctionsView(viewsets.ModelViewSet):
    queryset = GovernmentFunctions.objects.all()
    serializer_class = GovernmentFunctionsSerializer

class DailyBudgetView(viewsets.ModelViewSet):
    queryset = DailyBudget.objects.all()
    serializer_class = DailyBudgetSerializer






