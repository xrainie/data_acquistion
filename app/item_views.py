from django.shortcuts import redirect, render

from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404

from app.utils import query, query_or_get_objects_from_cache

from .models import Item

from .forms import ItemCreationForm, ItemEditForm

"""Здесь не использую CBV и встроенные представления авторизации django,
             иначе было бы показывать нечего:D"""

@login_required
def dashboard_items(request):
    users, items = query()

    context = {
        'users': users,
        'items': items,
        'select': 'items'
    }

    return render(request, 'items.html', context=context)


@login_required
def edit_item_view(request, id: int):
    users, items = query_or_get_objects_from_cache()
    item = get_object_or_404(Item, id=id)
    if request.method == 'POST':
        form = ItemEditForm(instance=item, data=request.POST)
        if form.is_valid():
            form.save()
        else:
            return render(request, 'manage/edit.html', {'form': form,
                                                        'object': 'Item',
                                                        'users': users,
                                                        'items': items,
                                                        'select': 'items'})
    if request.method == 'GET':
        form = ItemEditForm(instance=item)
        return render(request, 'manage/edit.html', {'form': form,
                                                    'object': 'Item',
                                                    'users': users,
                                                    'items': items,
                                                    'select': 'items'})
    return redirect(reverse_lazy('app:items'))


@login_required
def create_item(request):
    users, items = query_or_get_objects_from_cache()
    message = False
    if request.method == 'POST':
        form = ItemCreationForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.user = request.user
            item.save()
            message = True
    if request.method == 'GET':
        form = ItemCreationForm()
    return render(request, "manage/create.html", {'form': form,
                                               'message': message,
                                               'object': 'Item',
                                               'users': users,
                                               'items': items,
                                               'select': 'items'})


@login_required
def delete_item(request, id: int):
    users, items = query_or_get_objects_from_cache()
    if request.method == 'GET':
        return render(request, 'manage/delete_confirm.html', {'users': users,
                                                              'items': items,
                                                              'select': 'items'})
    if request.method == 'POST':
        item = get_object_or_404(Item, id=id)
        item.delete()
        return redirect(reverse_lazy('app:items'))