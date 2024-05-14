from django import forms
from .models import Post, Image

class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=['title','content']





# class MultipleFile(forms.ClearableFileInput):
#     allow_multiple_selected=True

# class ImageField(forms.FileField):
#     def __init__(self, *args, **kwargs):
#         kwargs.setdefault("widget", MultipleFile())
#         super().__init__(*args, **kwargs)
        
#     def clean(self, data, initial=None):
#         single_file_clean = super().clean
#         if not isinstance(data, (list,tuple)):
#             data = [data]
#         result = [single_file_clean(d, initial) for d in data]
#         return result

# class PostImage(forms.Form):
#     image = ImageField(required=False)
