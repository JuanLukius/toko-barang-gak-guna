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
        'class': 'PBP F'
    }

    return render(request, "main.html", context)
