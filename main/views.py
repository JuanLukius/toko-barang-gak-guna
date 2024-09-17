from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import render, redirect 
from main.forms import ItemEntryForm
from main.models import MagicItem
def create_item_entry(request):
    form = ItemEntryForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_item_entry.html", context)

def show_main(request):
    item_entries = MagicItem.objects.all()
    context = {
        'npm' : '2306216075',
        'name': 'Juan Lukius Barnaby',
        'class': 'PBP F',
        'item_entries' : item_entries
    }

    return render(request, "main.html", context)
def show_xml(request):
    data = MagicItem.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
def show_json(request):
    data = MagicItem.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
def show_xml_by_id(request, id):
    data = MagicItem.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
def show_json_by_id(request, id):
    data = MagicItem.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")