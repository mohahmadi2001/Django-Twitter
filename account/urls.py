from django.urls import path
from .views import UserLoginView,UserRegisterView,UserInfoView,UserEditInfoView,UserLogoutView,FollowUserView,FollowersView,FollowingsView,UnFollowUserView

app_name = "account"
urlpatterns = [
    path('login/',UserLoginView.as_view(),name="login_view"),
    path('register/',UserRegisterView.as_view(),name="register_view"),
    path("profile/",UserInfoView.as_view(),name="user_info_view"),
    path("edit/",UserEditInfoView.as_view(),name="edit_info_view"),
    path("logout/",UserLogoutView.as_view(),name="logout_view"),
    path('Follow/',FollowUserView.as_view(),name="follow_view"),
    path('Followers/',FollowersView.as_view(),name="follower_view"),
    path('Followings/',FollowingsView.as_view(),name="following_view"),
    path('unfollow/',UnFollowUserView.as_view(),name="unfollow_view"),
]
