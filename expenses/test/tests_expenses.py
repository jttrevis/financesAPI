from rest_framework.test import APITestCase
from expenses.models import Expenses
from django.urls import reverse
from rest_framework import status


class ExpensesTestCase(APITestCase):

    def setUp(self):
        self.list_url = reverse('Expenses-list')
        self.expenses_1 = Expenses.objects.create(
            date='2022-12-12', description='Test Rent 1', amount=1000, category_opt='Food'
        )
        self.expenses_2 = Expenses.objects.create(
            description='Test Car 2', amount=100
        )

        def test_get_expenses(self):
            """Test GET request"""
            response = self.client.get(self.list_url)
            self.assertEquals(response.status_code, status.HTTP_200_OK)

        def test_post_expenses(self):
            """Test POST request"""
            data = {

                'description': 'Test Car 2',
                'amount': 1000,

            }
            response = self.client.post(self.list_url, data=data)
            self.assertEquals(response.status_code, status.HTTP_201_CREATED)
