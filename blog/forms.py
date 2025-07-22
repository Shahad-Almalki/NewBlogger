from django import forms
from .models import Comments, Post

class NewComment(forms.ModelForm):
    class Meta:
         model = Comments
         fields = ('name','email','body')

class PostCreateForm(forms.ModelForm):
    title = forms.CharField(label='عنوان التدوينة')
    content = forms.CharField(label='نص التدوينة',widget=forms.Textarea)
    class Meta: 
        model = Post
        fields = ['title', 'content']
          
    
