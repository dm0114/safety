from django import forms
from .models import Suggestion, Comment


class SuggestionForm(forms.ModelForm):

    class Meta:
        model = Suggestion
        exclude = ('user', )


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('status', 'reason')
