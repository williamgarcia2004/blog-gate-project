from ..models.comment_model import Comment
from django import forms

class CommentForm(forms.ModelForm): 
    class Meta: 
        model = Comment 
        fields = ["body"]
        
        
