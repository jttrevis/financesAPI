from rest_framework.views import APIView
from django.db.models import Sum
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from expenses.models import Expenses
from income.models import Income


class SummaryViewSet(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, year, month):

        total_expenses = Expenses.objects.filter(
            date__year=year, date__month=month).aggregate(Sum('amount'))['amount__sum'] or 0
        total_income = Income.objects.filter(
            date__year=year, date__month=month).aggregate(Sum('amount'))['amount__sum'] or 0
        category_expenses = Expenses.objects.filter(date__year=year, date__month=month).values(
            'category').annotate(Total_Value=Sum('amount'))
        final_value = total_income - total_expenses

        return Response({
            'Expenses/Month': f'£{total_expenses}',
            'Income/Month': f'£{total_income}',
            'Total/Month': f'£{final_value}',
            'Total-By-Category': category_expenses
        })
