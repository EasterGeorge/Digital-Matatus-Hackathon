
from django import forms

from .models import Post

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column

from .models import Comment ,Reports



class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text','cover')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')

class ReportForm(forms.ModelForm):
    station_to = forms.CharField(required=False)
    class Meta:
        model = Reports
        occurrence_date = forms.DateField(
            widget=forms.TextInput(     
            attrs={'type': 'date'} 
        )) 
        fields = ('name', 'offense_description','station_from', 'station_to', 'sacco_name','occurrence_date')



