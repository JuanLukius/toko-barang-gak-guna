from django.urls import path
from main.views import show_main, create_item_entry, show_xml, show_json, show_xml_by_id, show_json_by_id
from main.views import register
from main.views import login_user
from main.views import logout_user
from main.views import edit_item
from main.views import delete_item
from main.views import add_item_entry_ajax


app_name = 'main'

urlpatterns = [
    path('delete/<uuid:id>', delete_item, name='delete_item'),
    path('logout/', logout_user, name='logout'),
    path('create-item-entry-ajax', add_item_entry_ajax, name='add_item_entry_ajax'),
    path('create-item-entry', create_item_entry, name='create_item_entry'),
    path('', show_main, name='show_main'),
    path('xml/', show_xml, name='show_xml'),
    path('register/', register, name='register'),
    path('json/', show_json, name='show_json'),
    path('edit-item/<uuid:id>', edit_item, name='edit_item'),
    path('login/', login_user, name='login'),
    path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
]