from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from apps.blog.models.post_model import Post

def home(request):
    return render(request, "core/home.html")

@login_required
def session_expired(request):
    return render(request, "auth/session_expired.html", {"url_name": "custom_auth:login"})

