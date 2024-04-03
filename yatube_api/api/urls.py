from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

v1_router = DefaultRouter()
v1_router.register(r'posts', PostViewSet)
v1_router.register(r'groups', GroupViewSet)
v1_router.register(r'follow', FollowViewSet)
v1_router.register(
    r'posts/(?P<post_id>\d+)/comments', CommentViewSet, basename='comment'
)

v1_urls = [
    path('', include(v1_router.urls)),
    path('', include('djoser.urls')),
    path('', include('djoser.urls.jwt')),
]

urlpatterns = [
    path('v1/', include(v1_urls)),
]
