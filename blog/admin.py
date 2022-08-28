from django.contrib import admin
from users.models import BlogUser
from .models import Post, Tag, Comment

class PostAdmin(admin.ModelAdmin):
     search_fields = ['title', 'intro', 'body']
     list_display = ['title', 'slug', 'tag', 'created_at']
     list_filter = ['tag', 'created_at']
     prepopulated_fields = {'slug': ('title',)}

class CommentAdmin(admin.ModelAdmin):
    list_display = [ 'detail']

admin.site.register(Post, PostAdmin)
admin.site.register(Tag)
admin.site.register(BlogUser)
admin.site.register(Comment, CommentAdmin )