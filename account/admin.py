from django.contrib import admin
from .models import User,Relation
# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display =['id','username','bio']
    search_fields =['username']
    

@admin.register(Relation)
class RelationAdmin(admin.ModelAdmin):
    pass

