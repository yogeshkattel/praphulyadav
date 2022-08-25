from django import forms

from .models import Post, News


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content','video_link', 'category']

        widgets = {
            'content': forms.Textarea(),
            'video_link': forms.Textarea(),
            'category': forms.Select(attrs={'class': 'form-control'}),
        }


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'content', 'image', 'post']

        widgets = {
            'content': forms.Textarea(),
        }
# subscribe form for the subscribe model
