from .models import Income
from .api.serializers import IncomeSerializer
from rest_framework import viewsets, generics


class IncomeViewSet(viewsets.ModelViewSet):
    queryset = Income.objects.all()
    serializer_class = IncomeSerializer


class IncomeList(generics.ListAPIView):
    def get_queryset(self):

        queryset = Income.objects.filter(
            date__year=self.kwargs['year'], date__month=self.kwargs['month'])
        return queryset
    serializer_class = IncomeSerializer
