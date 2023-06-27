from django.urls import path
from .views import UserView,ProfileView,FollowUserView,FollowersView,FollowingsView

app_name = "account"
urlpatterns = [
    path('users/',UserView.as_view(),name="show_users"),
    path('profile/',ProfileView.as_view(),name="profile"),
    path('Follow/',FollowUserView.as_view(),name="follow"),
    path('Followers/',FollowersView.as_view(),name="follower"),
    path('Followings/',FollowingsView.as_view(),name="following"),
]
