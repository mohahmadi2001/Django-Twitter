from django.shortcuts import render,get_object_or_404
from .models import User,Relation
from django.views import View
from django.contrib.auth.models import User
from .forms import UserLoginForm,UserRegisterForm
# Create your views here.

# class UserView(View):
#     def get(self,request):
#         users = User.get_users()
#         context = {'users': users}
#         return render(request, 'user_list.html', context)


# class ProfileView(View):
#     def get(self, request, username):
#         user = get_object_or_404(User, username=username)
#         profile = user.view_profile()
#         return render(request,"profile.html",profile)
    
class UserLoginView(View):
    form = UserLoginForm
    template = "accounts/login_view.html"
    def get(self,request):
        form = self.form
        context = {
            'form': form
        }
        return render(
            request=request,
            template_name=self.template,
            context=context,
        )
    def post(self,request):
        form = self.form(request.POST)
        if form.is_valid():
            pass
    
    
class UserRegisterView(View):
    pass


class FollowUserView(View):
    def post(self, request, username):
        user = get_object_or_404(User, username=username)
        if request.user.is_authenticated:
            if request.user != user:
                if Relation.objects.follow(request.user, user):
                    message = f'You are now following {username}'
                else:
                    message = f'You are already following {username}'
            else:
                message = 'You cannot follow yourself'
        else:
            message = 'You must be logged in to follow users'
        
        return render(request, 'follow_user.html', {'message': message})
    

class FollowersView(View):
    def get(self, request, username):
        user = get_object_or_404(User, username=username)
        followers = user.followers_count
        return render(request, 'followers.html', {'followers': followers})


class FollowingsView(View):
    def get(self, request, username):
        user = get_object_or_404(User, username=username)
        followings = user.followings_count
        return render(request, 'followings.html', {'followings': followings})
