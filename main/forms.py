from django.forms import ModelForm
from main.models import MagicItem

class ItemEntryForm(ModelForm):
    class Meta:
        model = MagicItem
        fields = ["name", "price", "description", "type"]