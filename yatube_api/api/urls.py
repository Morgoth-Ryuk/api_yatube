from rest_framework import routers
from rest_framework.authtoken import views
from django.urls import include, path
from .views import CommentViewSet, GroupViewSet, PostViewSet


router = routers.DefaultRouter()
router.register('posts', PostViewSet, basename='posts')
router.register('posts/(?P<post_id>\\d+)/comments', CommentViewSet,
                basename='comments')
router.register('groups', GroupViewSet, basename='groups')

urlpatterns = [
    path('api-token-auth/', views.obtain_auth_token),
    path('', include(router.urls)),
]
