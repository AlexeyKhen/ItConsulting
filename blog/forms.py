from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text', 'image', 'category']


class FilterForm(forms.Form):
    first_data = forms.DateTimeField(widget=forms.SelectDateWidget(attrs={'class': 'form-control'}))
    second_data = forms.DateTimeField(widget=forms.SelectDateWidget(attrs={'class': 'form-control'}))
