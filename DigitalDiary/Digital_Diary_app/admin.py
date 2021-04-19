from django.contrib import admin
from .models import Post
@admin.register(Post) #to register the post model 
class PostAdminModel(admin.ModelAdmin):
    list_display=['id','user','title','desc']
# Register your models here.
