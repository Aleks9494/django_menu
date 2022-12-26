from django.contrib import admin
from .models import Menu, MenuItem


class MenuItemInline(admin.TabularInline):
    model = MenuItem
    fields = ('menu', 'name', 'parent')
    extra = 1


class MenuAdmin(admin.ModelAdmin):
    model = Menu
    fieldsets = [
        ('MAIN MENU', {'fields': ['name']}),
    ]
    search_fields = ['name']
    inlines = [MenuItemInline]


admin.site.register(Menu, MenuAdmin)
