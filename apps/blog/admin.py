from django.contrib import admin
from .models.post_model import Post 
from .models.comment_model import Comment
from .models.post_model import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin): 
    list_display = ('title_post', 'image_post', 'author', 'status')
    list_filter = ('status', 'title_post')
    search_fields = ('title_post', 'author')
    prepopulated_fields = {"slug_title": ('title_post', )}
    show_facets = admin.ShowFacets.ALWAYS


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'post', 'created', 'active']
    list_filter = ['active', 'created', 'updated']
    search_fields = ['name', 'email', 'body']
    show_facets = admin.ShowFacets.ALWAYS