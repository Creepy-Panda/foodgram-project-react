from django.contrib.auth import get_user_model
from django.db.models import Sum
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions, status, viewsets
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from .filters import FavoriteFilter, IngredientFilter
from .models import (Favorite, Ingredient, IngredientAmount, Recipe,
                     ShoppingCart, Tag)
from .permissions import IsOwnerOrReadOnly
from .serializers import (CreateRecipeSerializer, FavoriteSerializer,
                          IngredientsSerializer, RecipeSerializer,
                          ShoppingCartSerializer, TagSerializer)

User = get_user_model()


class TagsViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = (permissions.AllowAny,)
    serializer_class = TagSerializer
    queryset = Tag.objects.all()
    pagination_class = None


class IngredientsViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = (permissions.AllowAny,)
    serializer_class = IngredientsSerializer
    pagination_class = None
    filter_backends = [DjangoFilterBackend]
    filterset_class = IngredientFilter
    queryset = Ingredient.objects.all()


class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    permission_classes = (IsOwnerOrReadOnly, )
    pagination_class = PageNumberPagination
    serializer_class = RecipeSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = FavoriteFilter

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return RecipeSerializer
        return CreateRecipeSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    @action(
        detail=True,
        methods=['POST', 'DELETE'],
        permission_classes=[permissions.IsAuthenticated, ]
    )
    def favorite(self, request, pk=None):
        if request.method == 'DELETE':
            return self.del_recipe(Favorite, request, pk)
        return self.add_recipe(Favorite, FavoriteSerializer,
                               request, pk
                               )

    @action(
        detail=True,
        methods=['POST', 'DELETE'],
        permission_classes=[permissions.IsAuthenticated, ]
    )
    def shopping_cart(self, request, pk=None):
        if request.method == 'DELETE':
            return self.del_recipe(ShoppingCart, request, pk)
        return self.add_recipe(ShoppingCart, ShoppingCartSerializer,
                               request, pk
                               )

    def add_recipe(self, model, serializer, request, pk):
        user = self.request.user
        recipe = get_object_or_404(Recipe, pk=pk)
        if model.objects.filter(user=user, recipe=recipe).exists():
            return Response(
                'Уже добавлено в корзину',
                status=status.HTTP_400_BAD_REQUEST
            )
        obj = model.objects.create(user=user, recipe=recipe)
        obj_serializer = serializer(obj, context={'request': request})
        return Response(obj_serializer.data, status=status.HTTP_201_CREATED)

    def del_recipe(self, model, request, pk):
        user = self.request.user
        recipe = get_object_or_404(Recipe, pk=pk)
        model.objects.filter(user=user, recipe=recipe).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(
        detail=False,
        permission_classes=[permissions.IsAuthenticated, ]
    )
    def download_shopping_cart(self, request):
        ingredients = IngredientAmount.objects.filter(
            recipe__shoppingcart__user=request.user
        ).values(
            'ingredient__name', 'ingredient__measurement_unit', 'amount'
        ).order_by(
            'ingredient__name'
        ).annotate(ingredient_total=Sum('amount'))
        file_name = 'shop_list.txt'
        lines = []
        for ingredient in ingredients:
            name = ingredient['ingredient__name']
            measurement_unit = ingredient['ingredient__measurement_unit']
            amount = ingredient['ingredient_total']
            lines.append(f'{name} {amount} ({measurement_unit})')
        content = '\n'.join(lines)
        content_type = 'text/plain,charset=utf8'
        response = HttpResponse(content, content_type=content_type)
        response['Content-Disposition'] = f'attachment; filename={file_name}'
        return response
