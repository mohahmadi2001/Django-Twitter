from django.contrib import admin
from .models import Post,Comment,Tag,Reaction,Image
# Register your models here.

class ImageInline(admin.TabularInline):
    model = Image
    extra = 1
    

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display =['id','text']
    search_fields =['username','text']
    inlines = [ImageInline]

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass

@admin.register(Reaction)
class ReactionAdmin(admin.ModelAdmin):
    pass

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    pass