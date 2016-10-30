from django.contrib import admin
from .models import Item
# Register your models here.
class ItemAdmin(admin.ModelAdmin):
	list_display = ['title', 'amount'] # make interface of Model 'Item' to the admin page.

admin.site.register(Item, ItemAdmin)