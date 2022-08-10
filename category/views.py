from .models import CategoryAPI
from .api.serializers import CategoryAPISerializer
from rest_framework import viewsets


class CategoryAPIViewSet(viewsets.ModelViewSet):
    queryset = CategoryAPI.objects.all()
    serializer_class = CategoryAPISerializer
