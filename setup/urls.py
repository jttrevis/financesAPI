from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from expenses.views import ExpensesViewSet
from income.views import IncomeViewSet
from category.views import CategoryAPIViewSet

routers = routers.SimpleRouter()
routers.register('income', IncomeViewSet)
routers.register('expenses', ExpensesViewSet)
routers.register('category', CategoryAPIViewSet)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(routers.urls)),
]
