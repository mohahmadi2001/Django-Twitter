from django.shortcuts import render,get_object_or_404
from .models import Post,Tag
from django.views import View
# Create your views here.

class PostView(View):
    def get(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)
        return render(request, 'post.html', {'post': post})


class TagView(View):
    def get(self, request, tag_id):
        tag = get_object_or_404(Tag, id=tag_id)
        return render(request, 'tag.html', {'tag': tag})