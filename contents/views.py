from typing import Any
from django import http
from django.shortcuts import render,get_object_or_404,redirect
from .models import Post,Tag,Image,Comment,Reaction
from django.views import View
from .forms import CreatePostForm,UpdatePostForm,CommentForm
# Create your views here.


class TagView(View):
    def post(self, request, post_id):
        tag_text = request.POST.get('tag_text')
        post = get_object_or_404(Tag, pk=post_id)
        post.add_tag(tag_text)
        return render(request,'post_detail.html', args=[post_id])
    
    
class RemoveTagView(View):
    def post(self, request, post_id):
        tag_text = request.POST.get('tag_text')
        post = get_object_or_404(Tag, pk=post_id)
        post.remove_tag(tag_text)
        return render(request,'post_detail.html', args=[post_id])
    

class ImageView(View):
   def post(self, request, post_id):
        image_file = request.FILES.get('image_file')
        post = get_object_or_404(Image, pk=post_id)
        post.add_image(image_file)
        return render(request,'post_detail.html', args=[post_id])


class RemoveImageView(View):
    def post(self, request, post_id, image_id):
        post = get_object_or_404(Image, pk=post_id)
        post.remove_image(image_id)
        return render(request,'post_detail.html', args=[post_id])
  

class ReactionView(View):
    def get(self, request, reaction_id):
        reaction = get_object_or_404(Reaction, id=reaction_id)
        return render(request, 'reaction_view.html', {'reaction': reaction})
    

class ArchivePostView(View):
    def post(self, request, post_id):
        post = get_object_or_404(Post, pk=post_id)
        post.archive()
        return render(request,'post_detail.html', args=[post_id])


class UnarchivePostView(View):
    def post(self, request, post_id):
        post = get_object_or_404(Post, pk=post_id)
        post.unarchive()
        return render(request,'post_detail.html', args=[post_id])


class PostListView(View):
    def get(self,request):
        posts = Post.objects.all()
        return render(
            request,
            "content:post_list.html",
            context={
                "posts":posts,
            },
        )


class PostDetailView(View):
    def get(self,request,id):
        post = Post.objects.get(id=id)
        comments = Post.comment_set.all()
        return render(
            request,
            "content/post_detail.html",
            context={
                "post":post,
                "comments":comments
            }
        )
        

class CreatePostView(View):
    def get(self, request):
        form = CreatePostForm()
        return render(request, 'create_post.html', {'form': form})
    
    def post(self, request):
        form = CreatePostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        return render(request, 'create_post.html', {'form': form})
    
    
class UpdatePostView(View):
    def setup(self, request, id) :
        self.this_post = get_object_or_404(Post, pk=id)
        return super().setup(request,id)
    
    def get(self, request):
        form = UpdatePostForm(instance= self.this_post)
        context ={
            'form': form,
            'post':  self.this_post,
        }
        return render(
            request,
            'update_post.html',
            context=context
            )
    
    def post(self, request):
        form = UpdatePostForm(request.POST, instance= self.this_post)
        if form.is_valid():
            form.save()
            return redirect('content:post_detail')
        context ={
            'form': form,
            'post':  self.this_post,
        }
        return render(
            request,
            'update_post.html',
            context=context
            )    
    
class CommentView(View):
    def post(self, request, post_id):
        post = get_object_or_404(Post, pk=post_id)
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('content:comment_view', post_id=post.id)
        return redirect('content:post_detail')

