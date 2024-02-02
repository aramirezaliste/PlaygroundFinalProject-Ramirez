from django import forms

from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'sub_title', 'body']
        widgets = {
            'title': forms.TextInput(
                attrs =  { 
                    'class':'form-control mb-3',
                    'placeholder':'Titulo'
                    }
                ),
            'sub_title': forms.TextInput(
                attrs =  { 
                    'class':'form-control mb-3',
                    'placeholder':'Sub Titulo'
                    }
                ),
            'body': forms.Textarea(
                attrs =  { 
                    'class':'form-control mb-3',
                    'rows': 3,
                    'placeholder':'Cuerpo',
                    }
                ),
        }
