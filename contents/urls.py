from django.urls import path
from .views import PostView,TagView,ImageView,CommentView,ReactionView,CreatePostView,UpdatePostView

app_name = "content"
urlpatterns = [
    path('posts/',PostView.as_view(),name="post_detail"),
    path('tags/',TagView.as_view(),name="tag_view"),
    path('images/',ImageView.as_view(),name="image_view"),
    path('reactions/',ReactionView.as_view(),name="reaction"),
    path('create/', CreatePostView.as_view(), name='create_post'),
    path('update/<int:post_id>/', UpdatePostView.as_view(), name='update_post'),
    path('comment/<int:post_id>/', CommentView.as_view(), name='comment'),
]
