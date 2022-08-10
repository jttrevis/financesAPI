from rest_framework import viewsets
from .models import Expenses
from .api.serializers import ExpensesSerializer


class ExpensesViewSet(viewsets.ModelViewSet):
    queryset = Expenses.objects.all()
    serializer_class = ExpensesSerializer
