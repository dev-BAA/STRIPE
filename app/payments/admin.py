from django.contrib import admin
from . import models


# Register your models here.
class ItemAdmin(admin.ModelAdmin):
    list_display = [field.name for field in models.Item._meta.fields]

    class Meta:
        model = models.Item


admin.site.register(models.Item, ItemAdmin)
