from django.contrib import admin
from .models import Post,Comment,Tag,Reaction,Image
# Register your models here.

class ImageInline(admin.TabularInline):
    model = Image
    extra = 1
    

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    fieldsets = (
        (
            None, {
                'fields': ('text', ('user', 'status', 'is_deleted'), 'tags'),
            },
        ),
    )
    list_display =['text','user','status']
    search_fields =['text']
    list_filter = ["status"]
    inlines = [ImageInline]
    
    @admin.action(description="This Action is Published Selected Post")
    def published_posts(self, request, queryset):
        queryset.update(status=Post.Statuses.PUBLISHED)
        self.message_user(request, 'Published Successfully')

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