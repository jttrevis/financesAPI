from rest_framework import viewsets, filters, generics
from django_filters.rest_framework import DjangoFilterBackend

from .models import Expenses
from .api.serializers import ExpensesSerializer


class ExpensesViewSet(viewsets.ModelViewSet):
    queryset = Expenses.objects.all()
    serializer_class = ExpensesSerializer

    filter_backends = [DjangoFilterBackend,
                       filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['date', 'description']
    ordering_fields = ['date']
    filterset_fields = ['description']


class ExpensesList(generics.ListAPIView):

    def get_queryset(self):

        queryset = Expenses.objects.filter(
            date__year=self.kwargs['year'], date__month=self.kwargs['month'])
        return queryset

    serializer_class = ExpensesSerializer
