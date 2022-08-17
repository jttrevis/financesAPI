from .models import CategoryAPI
from .api.serializers import CategoryAPISerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated


class CategoryAPIViewSet(viewsets.ModelViewSet):
    queryset = CategoryAPI.objects.all()
    serializer_class = CategoryAPISerializer
    permission_classes = [IsAuthenticated]
