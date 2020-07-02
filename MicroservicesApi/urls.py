from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from . import views


router = routers.DefaultRouter()
router.register("dailybudget", views.DailyBudgetView )
router.register("administrativebudget", views.AdministrativeView)
router.register("mbabudget", views.MDABudgetView)
router.register("economicrevenue", views.EconomicRevenueView)
router.register("economicexpenditure", views.EconomicExpenditureView )
router.register(" governmentfunctions", views.GovernmentFunctionsView)
router.register("expediture", views.store_economic_expenditure_values )
router.register("mda", views.store_mda_budget_values )


urlpatterns = [
	path('', include(router.urls)),
   
]
