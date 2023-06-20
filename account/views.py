from django.shortcuts import render
from .models import User
# Create your views here.

def user_list(request):
    users = User.get_users()
    context = {'users': users}
    return render(request, 'user_list.html', context)