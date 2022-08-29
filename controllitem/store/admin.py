from django.contrib import admin
from .models import ListItem, Item

class ChildItemInline(admin.TabularInline):
    model = Item
    fk_name = "child_item"
    readonly_fields = ("user", "list_item", "description", "quantity")
    exclude = ("deleted_at",)
    extra = 0
    max_num=0
    can_delete = False


class ItemInline(admin.TabularInline):
    model = Item
    fk_name = "list_item"
    readonly_fields = ("user", "list_item", "description", "quantity")
    exclude = ("deleted_at",)
    extra = 0
    max_num=0
    can_delete = False


class ItemAdmin(admin.ModelAdmin):
    search_fields = ("user", "list_item", "description")
    list_display = ("user", "list_item", "description", "quantity")
    list_filter = ("created_at", "updated_at", "deleted_at")
    fields = ("user", "list_item", "child_item", "description", "quantity")
    inlines = [ChildItemInline,]


class ListItemAdmin(admin.ModelAdmin):
    search_fields = ("user", "description", "created_at")
    list_display = ("user", "description")
    list_filter = ("created_at", "updated_at", "deleted_at")
    fields = ("user", "description")
    inlines = [ItemInline,]


admin.site.register(ListItem, ListItemAdmin)
admin.site.register(Item, ItemAdmin)
