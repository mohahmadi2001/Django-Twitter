from django.shortcuts import render,get_object_or_404
from .models import Post,Tag,Image,Comment,Reaction
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
    
    
class ImageView(View):
    def get(self, request, image_id):
        image = get_object_or_404(Image, id=image_id)
        return render(request, 'image.html', {'image': image})


class CommentView(View):
    def get(self, request, comment_id):
        comment = get_object_or_404(Comment, id=comment_id)
        return render(request, 'comment.html', {'comment': comment})
    

class ReactionView(View):
    def get(self, request, reaction_id):
        reaction = get_object_or_404(Reaction, id=reaction_id)
        return render(request, 'reaction.html', {'reaction': reaction})
    

class AddTagView(View):
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


class AddImageView(View):
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