from django.db import models
import pymongo 
# Create your models here.

class DailyBudget(models.Model):
    MDA_name = models.CharField(max_length=100)
    project_recipient_name = models.CharField(max_length=120)
    project_name = models.TextField()
    project_amount = models.FloatField()
    project_date = models.DateField()

    def ___str___(self):
        return self.MDA_name




class AdministrativeBudget(models.Model):
    sector = models.CharField(max_length=100, null=True)
    budget = models.FloatField(max_length=50, null=True)
    allocation = models.FloatField(max_length=50, null=True)
    total_allocation = models.FloatField(max_length=50, null=True)
    balance = models.FloatField(max_length=50, null=True)
    month = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.sector


"""
This model is to parse the data from the MDA in the Monthly Administrative Excel file into the Database. Each 
variable correlates to a column in the Database and Rows in the parsing excel file. The mda variable is to be filled 
with either of the mda in the excel file, budget variable is the Budget Amount budgeted for each mda, allocation 
variable is the amount released into for each mda for the month of MAY, total_allocation variable is the total amount 
released so far for each mda, balance variable is the amount left from each mda's Budget. The month variable 
automatically uploads the month. 
"""


class MDABudget(models.Model):
    mda = models.CharField(max_length=100, null=True)
    budget = models.FloatField(max_length=50, null=True)
    allocation = models.FloatField(max_length=50, null=True)
    total_allocation = models.FloatField(max_length=50, null=True)
    balance = models.FloatField(max_length=50, null=True)
    month = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.mda


"""
This model is to parse the data from the REVENUES in the Monthly Economic Excel file into the Database. Each 
variable correlates to a column in the Database and Rows in the parsing excel file. The name variable is to be 
filled with the name of revenues generated, revenue variable is the amount generated for the month of MAY, 
total_revenue variable is the total amount generated so far. The month variable automatically uploads the month.
"""


class EconomicRevenue(models.Model):
    name = models.CharField(max_length=100, null=True)
    revenue = models.FloatField(max_length=50, null=True)
    total_revenue = models.FloatField(max_length=50, null=True)
    month = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.name


"""
This model is to parse the data from the EXPENDITURES in the Monthly Economic Excel file into the Database. Each 
variable correlates to a column in the Database and Rows in the parsing excel file. The name variable is to be 
filled with the name of expenditures, budget variable is the Budget Amount budgeted, allocation variable is the spent 
for the month of MAY, total_allocation variable is the total amount spent so far, balance variable is the amount left 
from the Expenditures Budget. The month variable automatically uploads the month.
"""


class EconomicExpenditure(models.Model):
    name = models.CharField(max_length=100, null=True)
    budget = models.FloatField(max_length=50, null=True)
    allocation = models.FloatField(max_length=50, null=True)
    total_allocation = models.FloatField(max_length=50, null=True)
    balance = models.FloatField(max_length=50, null=True)
    month = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.name


"""This model is to parse the data from the FUNCTIONS OF GOVERNMENT excel file into the Database. Each 
variable correlates to a column in the Database and Rows in the parsing excel file. The name variable is to be filled 
with either of the government function in the excel file, budget variable is the Budget Amount budgeted for each 
government function, expenses variable is the amount spent by each mda for the month,balance variable is the 
amount left from each government function Budget.The percentage is the depicts the amount spent compared to amount given.
The month variable is the month when the transactions took place as one would think. 
"""


class GovernmentFunctions(models.Model):
    name = models.CharField(max_length=100, null=True)
    budget = models.FloatField(max_length=50, null=True)
    expenses = models.FloatField(max_length=50, null=True)
    total_expenses = models.FloatField(max_length=50, null=True)
    balance = models.FloatField(max_length=50, null=True)
    month = models.CharField(max_length=15, null=True)

    def __str__(self):
        return self.name


def monthly_file_handler(instance, file):
    return f'media/monthly/{file}'

class ExcelSaverModelMonthly(models.Model):
    monthly_file = models.FileField(upload_to=monthly_file_handler, null=True)