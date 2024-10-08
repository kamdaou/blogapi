from django.urls import path

from posts.views import PostDetail, PostList

urlpatterns = [
    path('<int:pk>', PostDetail.as_view(), name='post-detail'),
    path('', PostList.as_view(), name='post-list'),
]
