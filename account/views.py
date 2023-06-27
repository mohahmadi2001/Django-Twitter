from django.shortcuts import render,get_object_or_404
from .models import User
from django.views import View
# Create your views here.

class UserView(View):
    def get(self,request):
        users = User.get_users()
        context = {'users': users}
        return render(request, 'user_list.html', context)

class ProfileView(View):
    def get(self, request, username):
        user = get_object_or_404(User, username=username)
        profile = user.view_profile()
        return render(request,"profile.html",profile)