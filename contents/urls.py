from django.urls import path
from .views import UserView

app_name = "account"
urlpatterns = [
    path('users/',UserView.as_view(),name="show_users" ),
]
