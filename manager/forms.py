from django import forms
from .models import AttendanceList


class AttendanceListForm(forms.ModelForm):

    class Meta:
        model = AttendanceList
        exclude = ('created_at', 'user')

