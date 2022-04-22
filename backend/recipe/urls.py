from django.urls import include, path
from rest_framework.routers import DefaultRouter
from django.conf.urls.static import  static
from django.conf import settings

from .views import RecipeViewSet, TagsViewSet, IngredientsViewSet

router = DefaultRouter()
router.register('tags', TagsViewSet, basename='tags')
router.register('ingredients', IngredientsViewSet, basename='ingredients')
router.register('recipes', RecipeViewSet, basename='recipes')

urlpatterns = [
    path('', include(router.urls)),
]
