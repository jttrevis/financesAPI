from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from expenses.views import ExpensesViewSet
from income.views import IncomeViewSet
from category.views import CategoryAPIViewSet
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


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

routers = routers.SimpleRouter()
routers.register('income', IncomeViewSet)
routers.register('expenses', ExpensesViewSet)
routers.register('category', CategoryAPIViewSet)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(routers.urls)),
    path('swagger/', schema_view.with_ui('swagger',
         cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc',
         cache_timeout=0), name='schema-redoc'),
]
