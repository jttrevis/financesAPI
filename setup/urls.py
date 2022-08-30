from django.contrib import admin
from django.urls import path, include
from rest_framework import routers, permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


from summary.views import SummaryViewSet
from expenses.views import ExpensesViewSet, ExpensesList
from income.views import IncomeViewSet, IncomeList
from category.views import CategoryAPIViewSet
from user.views import UserViewSet

schema_view = get_schema_view(
    openapi.Info(
        title="FinancesAPI",
        default_version='v1',
        description="Finances API create with Django Rest Framework + PostgreSQL",
        terms_of_service="#",
        contact=openapi.Contact(email="jttrevis@outlook.com"),
        license=openapi.License(name="#"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

routers = routers.DefaultRouter()
routers.register('income', IncomeViewSet, basename='Income')
routers.register('expenses', ExpensesViewSet, basename='Expenses')
routers.register('category', CategoryAPIViewSet, basename='Category')
routers.register('register', UserViewSet, basename='Register')


urlpatterns = [
    path("", include(routers.urls)),
    path("admin/", admin.site.urls),
    path("api-auth/", include('rest_framework.urls')),
    path('expenses/<int:year>/<int:month>/', ExpensesList.as_view()),
    path('summary/<int:year>/<int:month>/', SummaryViewSet.as_view()),
    path('income/<int:year>/<int:month>/', IncomeList.as_view()),
    path('swagger/', schema_view.with_ui('swagger',
         cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc',
         cache_timeout=0), name='schema-redoc'),
]
