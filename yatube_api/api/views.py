from django.shortcuts import get_object_or_404
from rest_framework.filters import SearchFilter
from rest_framework.mixins import CreateModelMixin, ListModelMixin
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.serializers import ValidationError
from rest_framework.viewsets import (
    GenericViewSet,
    ModelViewSet,
    ReadOnlyModelViewSet,
)

from api.permissions import AuthorOrReadOnly, ReadOnly
from api.serializers import (
    CommentSerializer,
    FollowSerializer,
    GroupSerializer,
    PostSerializer,
)
from posts.models import Follow, Group, Post


class ListCreateViewSet(ListModelMixin, CreateModelMixin, GenericViewSet):
    pass


class ModelWithPermissionViewSet(ModelViewSet):
    permission_classes = (AuthorOrReadOnly,)

    def get_permissions(self):
        if self.action == 'retrieve':
            return (ReadOnly(),)
        return super().get_permissions()


class PostViewSet(ModelWithPermissionViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(ModelWithPermissionViewSet):
    serializer_class = CommentSerializer

    def get_queryset(self):
        post_id = self.kwargs.get('post_id')
        post = get_object_or_404(Post, pk=post_id)
        return post.comments

    def perform_create(self, serializer):
        post_id = self.kwargs.get('post_id')
        post = get_object_or_404(Post, pk=post_id)
        serializer.save(author=self.request.user, post=post)


class GroupViewSet(ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class FollowViewSet(ListCreateViewSet):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (SearchFilter,)
    search_fields = ('following__username',)

    def get_queryset(self):
        follows = Follow.objects.filter(user=self.request.user)
        return follows

    def perform_create(self, serializer):
        instanse = serializer.save(user=self.request.user)
        if instanse.user == instanse.following:
            raise ValidationError()
