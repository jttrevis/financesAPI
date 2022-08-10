from .models import Income
from .api.serializers import IncomeSerializer
from rest_framework import viewsets


class IncomeViewSet(viewsets.ModelViewSet):
    queryset = Income.objects.all()
    serializer_class = IncomeSerializer
