from django.urls import path
from .views import UserView,ProfileView

app_name = "account"
urlpatterns = [
    path('users/',UserView.as_view(),name="show_users"),
    path('profile/',ProfileView.as_view(),name="profile"),
]
