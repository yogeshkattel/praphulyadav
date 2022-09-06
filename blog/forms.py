from django import forms

from .models import Post, News


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content','video_link', 'category', 'is_published','is_notified','scheduleTime','schedule']

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

    # check if image is uploaded or not
  
    def clean_image(self):
        image = self.cleaned_data.get('image')
        if image:
            return image
        else:
            raise forms.ValidationError('Image is required')


    
