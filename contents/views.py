from django.shortcuts import render
from .models import Post
from django.views import View
# Create your views here.

class PostView(View):
    def get(self,request):
        posts = Post.get_posts()
        context = {'posts': posts}
        return render(request, 'post_list.html', context)