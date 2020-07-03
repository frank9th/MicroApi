from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
# import data
from .serializers import BudgetSerializer
import pandas
import xlrd
from django.shortcuts import render,redirect
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import os
from os import path, _exists
from rest_framework.parsers import FileUploadParser, MultiPartParser, FormParser
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt
from .models import MDABudget


import os
from django.core.files.storage import FileSystemStorage
# import pythoncom
# import win32com.client as win32
# from openpyxl import load_workbook
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

from .models import ExcelSaverModelMonthly, EconomicExpenditure


def looping(rows):
    lenght = len(rows)
    for i in range(lenght):
        row = rows[i]
        serializer = BudgetSerializer(data=row)
        if serializer.is_valid():

            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

                

# Create your views here.
def mainview(request):
    if request.method == 'GET':
        excel_data = request.GET.get('excel_data')         
        # excel_data = [{"mda":"Test","budget":100000,"allocation":27934783353.5,"total_allocation":686919637.6900000572,"balance":2106428472.8900001049},{"mda":"Test","budget":100000,"allocation":27934783353.5,"total_allocation":686919637.6900000572,"balance":2106428472.8900001049},{"mda":"Test","budget":100000,"allocation":27934783353.5,"total_allocation":686919637.6900000572,"balance":2106428472.8900001049}]
        # looping(excel_data)
        looping(excel_data)
    return JsonResponse(status=400)
    
def savemda(rows):
    lenght = len(rows)
    for i in range(lenght):
        row = rows[i]
        row['mda'] = MDABudget()
        row['mda'].mda = row['mda']
        row['mda'].budget = row['budget']
        row['mda'].allocation = row['allocation']
        row['mda'].total_allocation = row['total_allocation']
        row['mda'].balance = row['balance']
        row['mda'].save
        
        return JsonResponse(row['mda'] + "saved", status=201, safe=False)

# def savemda(rows):
#     arr = []
#     for i in range(len(rows)):
#         data = rows[i]
#         arr.append(
#         MDABudget(
#             name=data['mda'],
#             budget=data['budget'],
#             allocation=data['allocation'],
#             total_allocation=data['total_allocation'],
#             balance=data['balance']
#             )
#         )
#     MDABudget.objects.bulk_create(arr)

def savetest(rows):
    lenght = len(rows)
    for i in range(lenght):
        row = rows[i]
        row['name'] = EconomicExpenditure()
        row['name'].mda = str(row['name'])
        row['name'].budget = str(row['budget'])
        row['name'].allocation = str(row['allocation'])
        row['name'].total_allocation = str(row['total_allocation'])
        row['name'].balance = str(row['balance'])
        if row['name'].save():
            return JsonResponse(row['name'] + "saved", status=201, safe=False)
        else:
            return JsonResponse(row['name'] + "not saved", status=201, safe=False)

def save_test(rows):
    for i in range(rows):
        data = rows[i] 
        EconomicExpenditure.objects.create(name=data['name'],budget=data['budget'],allocation=data['allocation'],total_allocation=data['total_allocation'],balance=data['balance'])
        # EconomicExpenditure.objects.create(name=data['budget'])
        # EconomicExpenditure.objects.create(name=data['allocation'])
        # EconomicExpenditure.objects.create(name=data['total_allocation'])
        # EconomicExpenditure.objects.create(name=data['balance'])

def saver_test(rows):
    arr = []
    for i in range(len(rows)):
        data = rows[i]
        arr.append(
        EconomicExpenditure(
            name=data['name'],
            budget=data['budget'],
            allocation=data['allocation'],
            total_allocation=data['total_allocation'],
            balance=data['balance']
            )
        )
    EconomicExpenditure.objects.bulk_create(arr)

 


import pandas
import xlrd
from rest_framework import generics


# @api_view(['POST'])
# parser
@api_view(['POST' ])
def getexpenditurevalues(request):
        excel_files = request.FILES.getlist("excel_file")

        # a loop to get the files from the media folder
        for current_excel_file in excel_files:
            excel_file_name = current_excel_file.name
            current_file_path = f'media/monthly/{excel_file_name}'
            if os.path.exists(current_file_path):
                loc = current_file_path
                requiredvalues = []
                wb = xlrd.open_workbook(loc)
                sheet = wb.sheet_by_index(0)
                numrows = sheet.nrows
                numcols = sheet.ncols
                for i in range(numrows):
                    firstrowvalue = sheet.cell(i,0).value
                    if type(firstrowvalue) == str:
                        typeofdata = "string"
                        # print(str(firstrowvalue) + ' is of type ' + typeofdata)
                        if firstrowvalue.replace('.','',1).isdigit():
                            newfirstrowvalue = int(firstrowvalue)
                            if newfirstrowvalue > 20000000:
                                rowcheckvalue = newfirstrowvalue
                                rowdata = {'name': sheet.cell(i,1).value, 'budget' : sheet.cell(i,2).value, 'allocation' : sheet.cell(i,3).value, 'total_allocation' : sheet.cell(i,4).value, 'balance' : sheet.cell(i,5).value}
                                # print(rowdata)
                                requiredvalues.append(rowdata)
                # print(requiredvalues)
                saver_test(requiredvalues)
                return JsonResponse(requiredvalues, status=201, safe=False) 
            elif excel_file_name[-3:] == 'xls' or excel_file_name[-4:] == 'xlsx':
                ExcelSaverModelMonthly.objects.get_or_create(monthly_file=current_excel_file)

            # if request.method == 'POST':
                loc = current_file_path
                requiredvalues = []
                wb = xlrd.open_workbook(loc)
                sheet = wb.sheet_by_index(0)
                numrows = sheet.nrows
                numcols = sheet.ncols
                for i in range(numrows):
                    firstrowvalue = sheet.cell(i,0).value
                    if type(firstrowvalue) == str:
                        typeofdata = "string"
                        # print(str(firstrowvalue) + ' is of type ' + typeofdata)
                        if firstrowvalue.replace('.','',1).isdigit():
                            newfirstrowvalue = int(firstrowvalue)
                            if newfirstrowvalue > 20000000:
                                rowcheckvalue = newfirstrowvalue
                                rowdata = {'name': sheet.cell(i,1).value, 'budget' : sheet.cell(i,2).value, 'allocation' : sheet.cell(i,3).value, 'total_allocation' : sheet.cell(i,4).value, 'balance' : sheet.cell(i,5).value}
                                # print(rowdata)
                                requiredvalues.append(rowdata)
                # print(requiredvalues)
                saver_test(requiredvalues)
                return JsonResponse(requiredvalues, status=201, safe=False) 
            else:
                break

def savemda(rows):
    arr = []
    for i in range(len(rows)):
        data = rows[i]
        arr.append(
        MDABudget(
            mda=data['mda'],
            budget=data['budget'],
            allocation=data['allocation'],
            total_allocation=data['total_allocation'],
            balance=data['balance']
            )
        )
    MDABudget.objects.bulk_create(arr)

@api_view(['POST' ])
def getmdabudgetvalues(request):
        excel_files = request.FILES.getlist("excel_file")

        # a loop to get the files from the media folder
        for current_excel_file in excel_files:
            excel_file_name = current_excel_file.name
            current_file_path = f'media/monthly/{excel_file_name}'
            if os.path.exists(current_file_path):
                loc = current_file_path
                requiredvalues = []
                wb = xlrd.open_workbook(loc)
                sheet = wb.sheet_by_index(0)
                numrows = sheet.nrows
                numcols = sheet.ncols
                for i in range(numrows):
                    firstrowvalue = sheet.cell(i,0).value
                    if type(firstrowvalue) == str:
                        typeofdata = "string"
                        # print(str(firstrowvalue) + ' is of type ' + typeofdata)
                        if firstrowvalue.replace('.','',1).isdigit():
                            newfirstrowvalue = int(firstrowvalue)
                            if newfirstrowvalue > 100000000:
                                rowcheckvalue = newfirstrowvalue
                                rowdata = {'mda': sheet.cell(i,1).value, 'budget' : sheet.cell(i,2).value, 'allocation' : sheet.cell(i,3).value, 'total_allocation' : sheet.cell(i,4).value, 'balance' : sheet.cell(i,5).value}
                                # print(rowdata)
                                requiredvalues.append(rowdata)
                # print(requiredvalues)
                savemda(requiredvalues)
                return JsonResponse(requiredvalues, status=201, safe=False) 
            elif excel_file_name[-3:] == 'xls' or excel_file_name[-4:] == 'xlsx':
                ExcelSaverModelMonthly.objects.get_or_create(monthly_file=current_excel_file)

            # if request.method == 'POST':
                loc = current_file_path
                requiredvalues = []
                wb = xlrd.open_workbook(loc)
                sheet = wb.sheet_by_index(0)
                numrows = sheet.nrows
                numcols = sheet.ncols
                for i in range(numrows):
                    firstrowvalue = sheet.cell(i,0).value
                    if type(firstrowvalue) == str:
                        typeofdata = "string"
                        # print(str(firstrowvalue) + ' is of type ' + typeofdata)
                        if firstrowvalue.replace('.','',1).isdigit():
                            newfirstrowvalue = int(firstrowvalue)
                            if newfirstrowvalue > 100000000:
                                rowcheckvalue = newfirstrowvalue
                                rowdata = {'mda': sheet.cell(i,1).value, 'budget' : sheet.cell(i,2).value, 'allocation' : sheet.cell(i,3).value, 'total_allocation' : sheet.cell(i,4).value, 'balance' : sheet.cell(i,5).value}
                                # print(rowdata)
                                requiredvalues.append(rowdata)
                # print(requiredvalues)
                savemda(requiredvalues)
                return JsonResponse(requiredvalues, status=201, safe=False) 
            else:
                break
    # message = "Access Denied, must be a post method"
    # return JsonResponse(message, status=400, safe=False)





























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

