from django.core.cache import cache
from django.db.models import QuerySet

from app.models import CustomUser, Item

def query_or_get_objects_from_cache() -> list[QuerySet]:
    users = cache.get('users')
    if not users:
        users = CustomUser.objects.all()
        cache.set('users', users)
    items = cache.get('items')
    if not items:
        items = Item.objects.all()
        cache.set('items', items)
    return [users, items]