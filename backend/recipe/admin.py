from django.contrib import admin

from .models import Favorite, Recipe, ShoppingCart, Tag, Ingredients


class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'color')


class IngredientsAdmin(admin.ModelAdmin):
    list_display = ('name', 'measurement_unit')


admin.site.register(Recipe)
admin.site.register(Tag, TagAdmin)
admin.site.register(Ingredients, IngredientsAdmin)
admin.site.register(Favorite)
admin.site.register(ShoppingCart)
