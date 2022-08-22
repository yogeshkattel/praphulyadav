from django import forms

from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content','video_link', 'category']

        widgets = {
            'content': forms.Textarea(),
            'video_link': forms.Textarea(),
            'category': forms.Select(attrs={'class': 'form-control'}),
        }

# subscribe form for the subscribe model
