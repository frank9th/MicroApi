from django.shortcuts import render
import pymongo
from rest_framework.decorators import api_view
import json
import requests
from rest_framework import viewsets 
from .models import AdministrativeBudget, MDABudget, EconomicRevenue, EconomicExpenditure, GovernmentFunctions, DailyBudget, ExcelSaverModelMonthly
from .serializers import AdministrativeSerializer, MDABudgetSerializer, EconomicRevenueSerializer, EconomicExpenditureSerializer, GovernmentFunctionsSerializer, DailyBudgetSerializer 
from rest_framework.decorators import action
import os
import xlrd
from django.http import HttpResponse, JsonResponse


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









@api_view(['POST'])
def store_mda_budget_values(request):
    excel_files = request.FILES.getlist("excel_file")

    # a loop to get the files from the media folder
    for current_excel_file in excel_files:
        excel_file_name = current_excel_file.name

        current_file_path = f'media/monthly/{excel_file_name}'
        if excel_file_name[-3:] == 'xls' or excel_file_name[-4:] == 'xlsx':
            ExcelSaverModelMonthly.objects.get_or_create(monthly_file=current_excel_file)
            loc = current_file_path
            required_values = []
            wb = xlrd.open_workbook(loc)
            sheet = wb.sheet_by_index(0)
            num_rows = sheet.nrows
            num_cols = sheet.ncols
            for i in range(num_rows):
                first_row_value = sheet.cell(i, 0).value
                firstrow_value1 = str(sheet.cell(i,3).value)

                if not firstrow_value1.replace('.','',1).isdigit():
                    firstrow_value1 = firstrow_value1.replace('.','',1)
                    if not firstrow_value1.replace('-','',1).isdigit():
                        if firstrow_value1 != '':
                            firstrow_value1 = firstrow_value1[:3]
                            month = firstrow_value1

                if type(first_row_value) == str:
                    type_of_data = "string"
                    # print(str(first_row_value) + ' is of type ' + type_of_data)
                    if first_row_value.replace('.', '', 1).isdigit():
                        new_first_row_value = int(first_row_value)
                        if new_first_row_value > 100000000:
                            row_check_value = new_first_row_value
                            row_data = {'mda': sheet.cell(i, 1).value, 'budget': sheet.cell(i, 2).value,
                                        'allocation': sheet.cell(i, 3).value,
                                        'total_allocation': sheet.cell(i, 4).value,
                                        'balance': sheet.cell(i, 5).value, 'month' : month}
                            # print(row_data)
                            required_values.append(row_data)
            # print(required_values)
            save_mda(required_values)
            os.remove(current_file_path)
            return JsonResponse(required_values, status=201, safe=False)


'''
This is not a view function
It takes data extracted from MDA Budget excel sheet in the format below and saves them all to the database at once.
[{"mda": "LOSS ON INVENTORY", "budget": 2454037551812.8213, "allocation": 217515280304.7, 
"total_allocation": 854641653160.53, "balance": 1599395898652.2913}, {"mda": "IMPAIRMENT CHARGES - INVESTMENT PROPERTY 
- LAND & BUILDING - OFFICE", "budget": 1055706358677.2299, "allocation": 66004017316.47, 
"total_allocation": 333894644535.48, "balance": 721811714141.7499}]
'''


def save_mda(excel_output):
    arr = []
    for i in range(len(excel_output)):
        data = excel_output[i]
        if not MDABudget.objects.filter(
                mda=data['mda'],
                budget=data['budget'],
                allocation=data['allocation'],
                total_allocation=data['total_allocation'],
                balance=data['balance'],
                month=data['month']).exists():

            arr.append(
                MDABudget(
                    mda=data['mda'],
                    budget=data['budget'],
                    allocation=data['allocation'],
                    total_allocation=data['total_allocation'],
                    balance=data['balance'],
                    month=data['month']
                )
            )
    if arr != []:
        MDABudget.objects.bulk_create(arr)







@api_view(['POST'])
def store_economic_expenditure_values(request):
    excel_files = request.FILES.getlist("excel_file")

    # a loop to get the files from the media folder
    for current_excel_file in excel_files:
        excel_file_name = current_excel_file.name
        current_file_path = f'media/monthly/{excel_file_name}'
        if excel_file_name[-3:] == 'xls' or excel_file_name[-4:] == 'xlsx':
            ExcelSaverModelMonthly.objects.get_or_create(monthly_file=current_excel_file)
            loc = current_file_path
            required_values = []
            wb = xlrd.open_workbook(loc)
            sheet = wb.sheet_by_index(0)
            num_rows = sheet.nrows
            num_cols = sheet.ncols
            for i in range(num_rows):
                first_row_value = sheet.cell(i, 0).value

                firstrow_value1 = str(sheet.cell(i,3).value)

                if not firstrow_value1.replace('.','',1).isdigit():
                    firstrow_value1 = firstrow_value1.replace('.','',1)
                    if not firstrow_value1.replace('-','',1).isdigit():
                        if firstrow_value1 != '':
                            firstrow_value1 = firstrow_value1[:3]
                            month = firstrow_value1

                if type(first_row_value) == str:
                    type_of_data = "string"
                    # print(str(first_row_value) + ' is of type ' + type_of_data)
                    if first_row_value.replace('.', '', 1).isdigit():
                        new_first_row_value = int(first_row_value)
                        if new_first_row_value > 20000000:
                            row_check_value = new_first_row_value
                            row_data = {'name': sheet.cell(i, 1).value, 'budget': sheet.cell(i, 2).value,
                                        'allocation': sheet.cell(i, 3).value,
                                        'total_allocation': sheet.cell(i, 4).value,
                                        'balance': sheet.cell(i, 5).value, 'month' : month}
                            # print(row_data)
                            required_values.append(row_data)
            # print(required_values)
            economic_expenditure_data(required_values)
            os.remove(current_file_path)
            return JsonResponse(required_values, status=201, safe=False)




def economic_expenditure_data(current_excel_file):
    arr = []
    for i in range(len(current_excel_file)):
        data = current_excel_file[i]
        if not EconomicExpenditure.objects.filter(
                name=data['name'],
                budget=data['budget'],
                allocation=data['allocation'],
                total_allocation=data['total_allocation'],
                balance=data['balance'],
                month=data['month']
        ).exists():
            arr.append(
                EconomicExpenditure(
                    name=data['name'],
                    budget=data['budget'],
                    allocation=data['allocation'],
                    total_allocation=data['total_allocation'],
                    balance=data['balance'],
                    month=data['month']
                )
            )
    if arr != []:
        EconomicExpenditure.objects.bulk_create(arr)