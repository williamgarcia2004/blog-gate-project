from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.utils.text import slugify

from taggit.managers import TaggableManager

User = get_user_model()

class PostStatusManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Post.Status.PUBLISHED) 
    
class Post(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'
        
    # Object managers 
    objects = models.Manager()    # por defecto
    published = PostStatusManager()    
    
    tags = TaggableManager()
    # Atributos
    title_post = models.CharField(max_length=150)
    slug_title = models.SlugField(unique=True, blank=True, null=True)
    image_post = models.ImageField(upload_to="image-post/")
    publish = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)
    
    """
        Si no se coloca 'related_name', por defecto la relación inversa entre los modelos será con 'nombremodelo_set'
    """
    
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="blog_posts"
    )
    
    body = models.TextField()
    status = models.CharField(
        max_length=2, 
        choices=Status,
        default=Status.DRAFT
    )
    
    class Meta:
        indexes = [
            models.Index(fields=['author', 'title_post'])
        ]
        
        ordering = ["id"]
      
    def save(self, *args, **kwargs):
        if not self.slug_title:
            base_slug = slugify(self.title_post)
            slug_title = base_slug
            n = 1
            while Post.objects.filter(slug_title=slug_title).exists():
                slug_title = f"{base_slug}-{n}"
                n += 1
            self.slug_title = slug_title
        super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse("blog:post_detail", args=[self.slug_title])
    
    def __str__(self):
        return self.title_post
    