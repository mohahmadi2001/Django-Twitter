from django.shortcuts import render,redirect,get_object_or_404
from .models import User,Relation
from django.views import View
from .forms import UserLoginForm,UserRegisterForm,UserEditInfoForm
from django.contrib.auth import login,logout
# Create your views here.

    
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
        form = self.form(request.POST,request=request)
        if form.is_valid():
            user = form.cleaned_data["user"]
            login(request=request, user=user)
            return redirect("account:user_info_view")
        context = {
            "form": form
        }
        return render(request=request,
                      template_name=self.template,
                      context=context
        )

    
class UserRegisterView(View):
    form = UserRegisterForm
    template = "accounts/register-view.html"
    def get(self, request):
        form = self.form
        context = {
            "form": form
        }
        return render(
            request=request, 
            template_name=self.template, 
            context=context, 
        )

    def post(self, request):
        status = 200
        form = self.form(request.POST, request=request)
        if form.is_valid():
            user = form.cleaned_data["user"]
            user = form.save(commit=True)
            login(request=request, user=user)
            return redirect("accounts:user_info_view")
        else:
            status = 400

        context = {
            "form": form
        }
        return render(
            request=request, 
            template_name=self.template, 
            context=context, 
            status=status,
        )


class UserInfoView(View):
     def get(self, request, username):
        user = get_object_or_404(User, username=username)
        profile = user.view_profile()
        return render(
            request,
            "accounts/user-info.html",
            profile
            )


class UserLogoutView(View):
        def get(self,request):
            logout(request)
            return redirect("accounts:user_info_view")


class UserEditInfoView: 
    form = UserEditInfoForm
    template = "accounts/edit-info-view.html"
    def get(self, request):
        form = self.form(instance=request.user)
        context = {
            "form": form
        }
        return render(
            request=request,
            template_name=self.template,
            context=context
        )

    def post(self, request):
        form = self.form(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("accounts:user_info_view")

        context = {
            "form": form
        }
        return render(
            request=request,
            template_name=self.template,
            context=context
        )


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
        
        return render(request, 'follow_user_view.html', {'message': message})
    

class FollowersView(View):
    def get(self, request, username):
        user = get_object_or_404(User, username=username)
        followers = user.followers_count
        return render(request, 'followers_view.html', {'followers': followers})


class FollowingsView(View):
    def get(self, request, username):
        user = get_object_or_404(User, username=username)
        followings = user.followings_count
        return render(request, 'followings_view.html', {'followings': followings})


class UnFollowUserView(View):
    def post(self, request, user_id):
        user = User.objects.get(id=user_id)
        current_user = request.user
        current_user_relation = Relation.objects.filter(from_user=current_user, to_user=user).first()
        if current_user_relation:
            current_user_relation.delete()
            return redirect("accounts:user_info_view", user_id=user_id)
        else:
            return redirect("accounts:user_info_view", user_id=user_id)
