from django.contrib import admin
from .models import EconomicExpenditure, EconomicExpenditure1, MDABudget

# Register your models here.
admin.site.register(EconomicExpenditure)
admin.site.register(EconomicExpenditure1)
admin.site.register(MDABudget)
