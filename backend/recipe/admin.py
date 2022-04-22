from django.contrib import admin

from .models import Favorite, Ingredient, Recipe, ShoppingCart, Tag


class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'color')


class IngredientsAdmin(admin.ModelAdmin):
    list_display = ('name', 'measurement_unit')


admin.site.register(Recipe)
admin.site.register(Tag, TagAdmin)
admin.site.register(Ingredient, IngredientsAdmin)
admin.site.register(Favorite)
admin.site.register(ShoppingCart)
