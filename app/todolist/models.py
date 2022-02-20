from django.db import models

class ItemModel(models.Model):
    id = models.UUIDField(primary_key=True)
    name = models.TextField(max_length=100)

    def __str__(self):
        return self.name