from rest_framework import routers
from rest_framework.authtoken import views
from django.urls import include, path
from api.views import CommentViewSet, GroupViewSet, PostViewSet


v1_router = routers.DefaultRouter()
v1_router.register('posts', PostViewSet, basename='posts')
v1_router.register(
    'posts/(?P<post_id>\\d+)/comments', CommentViewSet,
    basename='comments'
)
v1_router.register('groups', GroupViewSet, basename='groups')

urlpatterns = [
    path('api-token-auth/', views.obtain_auth_token),
    path('v1/', include(v1_router.urls)),
]
