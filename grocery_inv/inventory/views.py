from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404
from django.contrib.auth.decorators import login_required

from .models import GroceryItem, GroceryList
from .forms import GroceryItemForm, GroceryListForm

def index(request):
    """The home page for Grocery Inventory."""
    return render(request, 'inventory/index.html')

@login_required
def inventory(request):
    """Show all inventory"""
    grocery_item = GroceryItem.objects.filter(owner=request.user)
    context = {'grocery_item': grocery_item}
    return render(request, 'inventory/inventory.html', context)

@login_required
def add_item(request):
    """Add a new item."""
    form = GroceryItemForm(request.POST or None)
    if form.is_valid():
        new_item = form.save(commit=False)
        new_item.owner = request.user
        new_item.save()
        return redirect('inventory:inventory')

    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'inventory/add_item.html', context)

@login_required
def edit_item(request, pk):
    """Edit an item."""
    try:
        item = GroceryItem.objects.get(id=pk)
    except:
        raise Http404
    if item.owner != request.user:
        raise Http404
    if request.method == 'POST':
        # Initial request; pre-fill form with the current entry.
        form = GroceryItemForm(instance=item, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('inventory:inventory')

    else:
        # POST data submitted; process data.
        form = GroceryItemForm(instance=item)

    # Display a blank or invalid form.
    context = {'item': item,'form': form}
    return render(request, 'inventory/edit_item.html', context)

@login_required
def delete_item(request, pk):
    """Delete an item."""
    try:
        item = GroceryItem.objects.get(id=pk)
    except:
        raise Http404
    if item.owner != request.user:
        raise Http404
    GroceryItem.objects.filter(id=pk).delete()
    items = GroceryItem.objects.all()

    # Redirect to inventory page with updated items after delete
    return redirect('inventory:inventory')
