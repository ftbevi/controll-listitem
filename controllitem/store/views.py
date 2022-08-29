from rest_framework import permissions, viewsets
from .serializers import ItemSerializer, ListItemSerializer

from .models import ListItem, Item


class ListItemViewSet(viewsets.ModelViewSet):
    queryset = ListItem.objects.all().order_by('-created_at')
    serializer_class = ListItemSerializer
    permission_classes = [permissions.AllowAny]


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all().order_by('-created_at')
    serializer_class = ItemSerializer
    permission_classes = [permissions.AllowAny]
