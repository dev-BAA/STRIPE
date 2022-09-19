from django.contrib import admin
from . import models


# Register your models here.
class ItemAdmin(admin.ModelAdmin):
    list_display = [field.name for field in models.Item._meta.fields]

    class Meta:
        model = models.Item
class OrderAdmin(admin.ModelAdmin):
    list_display = [field.name for field in models.Order._meta.fields]

    class Meta:
        model = models.Order

class TaxAdmin(admin.ModelAdmin):
    list_display = [field.name for field in models.Tax._meta.fields]

    class Meta:
        model = models.Tax

admin.site.register(models.Item, ItemAdmin)
admin.site.register(models.Order, OrderAdmin)
admin.site.register(models.Tax, TaxAdmin)
