from django_filters.rest_framework import FilterSet, filters

from .models import Ingredients, Recipe


class IngredientFilter(FilterSet):
    name = filters.CharFilter(lookup_expr='istartswith')

    class Meta:
        model = Ingredients
        fields = ('name',)


class FavoriteFilter(FilterSet):
    is_favorited = filters.BooleanFilter(method='get_is_favorited')

    class Meta:
        model = Recipe
        fields = ('is_favorited',)

    def get_is_favorited(self, queryset, name, value):
        if value is True and self.request.user.is_authenticated:
            return queryset.filter(favorite__user=self.request.user)
        return queryset
