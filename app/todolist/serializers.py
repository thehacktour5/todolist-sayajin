from rest_framework import serializers
from app.todolist.models import ItemModel

class ItemSerializer(serializers.ModelSerializer):
    model = ItemModel
    fields = "__all__"