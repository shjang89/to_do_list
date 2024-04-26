from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
  class Meta:
    model = Article 
    fields = '__all__'
    widgets = {
    'title': forms.TextInput(attrs={
      'class': 'form-control',
      'style': 'width:500px;',
      'placeholder': '글 제목을 입력하세요'
      }),
    'content': forms.Textarea(attrs={
      'class': 'form-control',
      'style': 'width:500px;',
      'placeholder': '글 내용을 입력하세요'
      }),
    }