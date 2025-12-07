from django import template 
from django.contrib.auth import get_user_model

from ..models.post_model import Post 

register = template.Library()
User = get_user_model()

@register.simple_tag
def total_posts (): 
    return Post.published.count()