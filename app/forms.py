from django.forms import ModelForm
from app.models import Comment


class CommentForm(ModelForm):
    """Formulaire de commentaires d'article"""
    class Meta:
        model = Comment
        fields = ('comment', )
