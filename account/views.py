from django.shortcuts import render
from .models import User
from django.views import View
# Create your views here.

class UserView(View):
    def get(request):
        users = User.get_users()
        context = {'users': users}
        return render(request, 'user_list.html', context)