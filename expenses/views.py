from rest_framework import viewsets, filters
from .models import Expenses
from .api.serializers import ExpensesSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics


class ExpensesViewSet(viewsets.ModelViewSet):
    queryset = Expenses.objects.all()
    serializer_class = ExpensesSerializer

    filter_backends = [DjangoFilterBackend,
                       filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['date', 'description']
    ordering_fields = ['date']
    filterset_fields = ['description', 'date']
