from django.urls import path, include
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from .views import mainview, getexpenditurevalues, getmdabudgetvalues, store_economic_expenditure_values, store_mda_budget_values

# router = routers.DefaultRouter()
# router.register("home", views.BudgetView)
# router.register("daily-payment-report", views.daily_payment_report_view),
# router.register("daily_reports_view", views.get_daily_reports_view),


urlpatterns = [
    # path("", include(router.urls)),
    path('test/', mainview),
    path('values/', getexpenditurevalues),
    path('mda/', getmdabudgetvalues),
    path('mda1/', store_mda_budget_values),
    path('expense/', store_economic_expenditure_values),
]
