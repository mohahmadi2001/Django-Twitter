from django.urls import path
from .views import PostView,TagView,ImageView

app_name = "account"
urlpatterns = [
    path('posts/',PostView.as_view(),name="post"),
    path('tags/',TagView.as_view(),name="tag"),
    path('images/',ImageView.as_view(),name="image"),
    path('comments/',ImageView.as_view(),name="comment"),

]
