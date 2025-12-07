from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from apps.blog.models.post_model import Post
from ..forms.post_form import PostForm
from apps.blog.models.comment_model import Comment 
from ..forms.comment_form import CommentForm

from apps.core.utils.markdown_format import render_markdown
from taggit.models import Tag

@login_required
def post_list(request, tag_slug=None): 
    post_list = Post.published.all()
    
    tag = None 
    if tag_slug: 
        tag = get_object_or_404(Tag, slug=tag_slug)
        post_list = post_list.filter(tags__in=[tag])
        
    
    paginator = Paginator(post_list, 3)
    page_number = request.GET.get('page')
    
    try:
        posts = paginator.page(page_number)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
        
    return render(
        request,
        'blog/list.html',
        {'posts': posts, "tag": tag}
    )

@login_required
def post_detail(request, post):
    post = get_object_or_404(
        Post,
        slug_title=post,
        status=Post.Status.PUBLISHED
    )
    
    # Atributo temporal en tiempo de ejecución
    post.body_html = render_markdown(post.body)
    
    comments = post.comments.filter(active=True).order_by("-created")
    new_comment = None 
    
    if request.method == "POST": 
        form = CommentForm(data=request.POST)
        
        if form.is_valid(): 
            new_comment = form.save(commit=False)
            new_comment.post = post
            new_comment.name = request.user.get_full_name() 
            new_comment.email = request.user.email 
            new_comment.save()
            
            return redirect('blog:post_detail', post=post.slug_title)
    else: 
        form = CommentForm()
            
        
    return render(
        request,
        'blog/detail.html',
        {
            'post': post, 
            "comments": comments, 
            "form": form
        }
    )

@login_required
def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
                
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            form.save_m2m() 
                     
            return redirect("blog:post_list") 
    else:
        form = PostForm()
    
    return render(request, "blog/create.html", {"form": form})

@login_required
def update_post(request, post): 
    post = get_object_or_404(
        Post, 
        slug_title=post,
        # Solo el autor original del post pueda editar o eliminar su contenido.
        author=request.user    
    )

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        
        if form.is_valid():
            updated_post = form.save(commit=False)
            updated_post.save()
            form.save_m2m()
            
            return redirect("blog:post_list")
    else: 
        form = PostForm(instance=post) 
        
    return render(request, "blog/update.html", {"form": form, "post": post})
    
@login_required
def delete_post(request, post):
    post = get_object_or_404(
        Post, 
        slug_title=post,
        # Solo el autor original del post pueda editar o eliminar su contenido.
        author=request.user
    )
    
    if request.method == "POST":
        post.delete()
        
        return redirect("blog:post_list")
    
    return render(request, "blog/delete.html", {"post": post})