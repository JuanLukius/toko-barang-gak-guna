from django.db import models
import uuid
class MagicItem(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  # tambahkan baris ini
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    type = models.TextField()

    @property
    def is_not_a_waste_of_money(self):
        return self.price == 0