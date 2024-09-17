from django.urls import path
from main.views import show_main, create_item_entry

app_name = 'main'

urlpatterns = [
    path('create-item-entry', create_item_entry, name='create_item_entry').
    path('', show_main, name='show_main'),
]