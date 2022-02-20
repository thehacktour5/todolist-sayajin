from rest_framework import viewsets

from app.todolist.models import ItemModel
from app.todolist.serializers import ItemSerializer

class ItemViewSet(viewsets.ModelViewSet):
    querset = ItemModel.objects.all()
    serializer_class = ItemSerializer