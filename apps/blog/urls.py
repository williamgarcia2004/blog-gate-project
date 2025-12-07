from django.urls import path
from .views.blog_views import  post_list, post_detail, create_post, update_post, delete_post

app_name = "blog"

urlpatterns = [
    path("tag/<slug:tag_slug>/", post_list, name="post_list_by_tag"), 
    path("create_post/", create_post, name="create_post"),
    path("post_list/", post_list, name="post_list"),
    path("<slug:post>/", post_detail, name="post_detail"),
    path("update_post/<slug:post>/", update_post, name="update_post"), 
    path("delete_post/<slug:post>/", delete_post, name="delete_post")
]