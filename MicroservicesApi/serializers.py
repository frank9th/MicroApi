
from rest_framework import serializers
from .models import AdministrativeBudget, MDABudget, EconomicRevenue, EconomicExpenditure, GovernmentFunctions, DailyBudget

class AdministrativeSerializer(serializers.ModelSerializer):
	class Meta:
		model = AdministrativeBudget
		fields = "__all__"

class MDABudgetSerializer(serializers.ModelSerializer):
	class Meta:
		model = MDABudget
		fields = "__all__"

class EconomicRevenueSerializer(serializers.ModelSerializer):
	class Meta:
		model = EconomicRevenue
		fields = "__all__"

class EconomicExpenditureSerializer(serializers.ModelSerializer):
	class Meta:
		model = EconomicExpenditure
		fields = "__all__"


class GovernmentFunctionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = GovernmentFunctions
        fields = ['id','name', 'budget', 'expenses', 'total_expenses', 'balance', 'month', ]

class DailyBudgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyBudget
        fields = ['id','MDA_name', 'project_recipient_name', 'project_name', 'project_amount', 'project_date',]


 
     
     
     
     