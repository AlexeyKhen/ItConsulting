from django import forms
from django.contrib.auth import get_user_model

from .models import Post

User = get_user_model()


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text', 'image', 'category']


class FilterForm(forms.Form):
    first_data = forms.DateTimeField(widget=forms.SelectDateWidget(attrs={'class': 'form-control'}))
    second_data = forms.DateTimeField(widget=forms.SelectDateWidget(attrs={'class': 'form-control'}))
    user = forms.ModelChoiceField(queryset=User.objects.all(), widget=forms.Select)
