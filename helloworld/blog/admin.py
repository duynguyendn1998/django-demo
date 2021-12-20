from django.contrib import admin
from .models import Posts, Comments

# Setting display for Posts
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_dt'] # display column title & created_dt
    list_filter = ['created_dt'] # filter by created_dt column
    search_fields = ['title'] #  search by titel column

admin.site.register(Posts, PostAdmin) # registion model with setting display PostAdmin

#setting display for comments
class CommentAdmin(admin.ModelAdmin):
    list_display = ['content_comment','user_name','created_dt']
admin.site.register(Comments, CommentAdmin)