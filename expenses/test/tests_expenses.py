from rest_framework.test import APITestCase
from expenses.models import Expenses
from django.urls import reverse
from rest_framework import status


class ExpensesTests(APITestCase):
    url = reverse('Expenses-list')

    def test_create_expenses(self):
        """Test POST  request - Expense"""
        data = {
            'description': 'Test01',
            'date': '2022-01-01',
            'amount': 1000,
            'category_opt': 'Other',
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Expenses.objects.count(), 1)
        self.assertEqual(Expenses.objects.get().description, 'Test01')

    def test_get_expenses(self):
        """Test GET request - Expenses"""
        url = reverse('Expenses-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_put_expenses(self):
        """Test PUT request - Expense"""
        data = {
            'description': 'Test0attt',
            'date': '2022-01-01',
            'amount': 1000,
            'category_opt': 'Other',
        }
        response = self.client.put(self.url + '1', data=data)
        self.assertEqual(response.status_code,
                         status.HTTP_301_MOVED_PERMANENTLY)

    def test_delete_expenses(self):
        """Test DELETE - Expense"""

        response = self.client.delete('/expenses/1/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
