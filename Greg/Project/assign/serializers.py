# serializers convert the data in our db to and from js 
# and serve them unto our web pages 

from rest_framework import serializers
from .models import MDABudget


class BudgetSerializer(serializers.ModelSerializer):
	class Meta:
		model = MDABudget
		fields = ('id', 'mda', 'budget', 'allocation', 'total_allocation', 'balance')
