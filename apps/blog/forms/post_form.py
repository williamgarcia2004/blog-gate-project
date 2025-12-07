from django import forms
from ..models.post_model import Post  
from apps.blog.validators.title import validar_title
from taggit.forms import TagWidget

class PostForm(forms.ModelForm):
    title_post = forms.CharField(
        required=True, 
        max_length=150,
        validators=[validar_title],
        widget=forms.TextInput(
            attrs={
                "placeholder": "Título del post",
                "minlength": "10",
                "maxlength": "150",
            }
        )
    )
    
    image_post = forms.ImageField(
        required=True,
    )
    
    body = forms.CharField(
        required=True, 
        widget=forms.Textarea(
            attrs={
                "placeholder": "Body",
            }
        )
    )

    class Meta:
        model = Post
        fields = ["tags", "title_post", "image_post", "author", "body", "status"]
        widgets = {
            "tags": TagWidget(
                attrs={
                    "placeholder": "Tags separados por coma",
                }
            )
        }
    