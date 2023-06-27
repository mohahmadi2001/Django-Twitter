from django.urls import path
from .views import PostView,TagView

app_name = "account"
urlpatterns = [
    path('posts/',PostView.as_view(),name="post"),
    path('tags/',TagView.as_view(),name="tag"),

]
