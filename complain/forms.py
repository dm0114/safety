from django import forms
from .models import Complain, ComplainComment


class ComplainForm(forms.ModelForm):

    class Meta:
        model = Complain
        exclude = ('user', )


class ComplainCommentForm(forms.ModelForm):

    class Meta:
        model = ComplainComment
        fields = ('title', 'content')
