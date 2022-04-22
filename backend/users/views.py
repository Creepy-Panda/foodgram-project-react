from django.contrib.auth import get_user_model
from djoser.views import UserViewSet
from rest_framework import permissions, status
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from .models import Follow
from .serializers import CustomUserSerializer, FollowSerializer

User = get_user_model()


class CustomUserViewSet(UserViewSet):
    serializer_class = CustomUserSerializer

    @action(detail=False,
            methods=['get'],
            permission_classes=(permissions.IsAuthenticated,)
            )
    def subscriptions(self, request):
        user = request.user
        queryset = Follow.objects.filter(user=user)
        pages = self.paginate_queryset(queryset)
        serializer = FollowSerializer(
            pages, many=True, context={'request': request}
        )
        return self.get_paginated_response(serializer.data)

    @action(
        methods=['POST', 'DELETE'],
        detail=True,
        permission_classes=(permissions.IsAuthenticated, )
    )
    def subscribe(self, request, id=None):
        author = get_object_or_404(User, id=id)
        user = request.user
        if request.method == 'POST':
            if user == author:
                return Response(
                    'Вы не можете подписаться на самого себя',
                    status=status.HTTP_400_BAD_REQUEST
                    )
            if Follow.objects.filter(user=user, author=author).exists():
                return Response(
                    'Подписка оформлена',
                    status=status.HTTP_400_BAD_REQUEST
                    )
            follow = Follow.objects.create(user=user, author=author)
            serializer = FollowSerializer(
                follow, context={'request': request}
                )
        if request.method == 'DELETE':
            Follow.objects.filter(user=user, author=author).delete()
            return Response(
                'Успешно отписались',
                status=status.HTTP_204_NO_CONTENT
                )
        return Response(serializer.data, status=status.HTTP_201_CREATED)
