from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        label = "제목",
        widget = forms.TextInput(
            attrs={
                'class' : 'mt-3 fw-bold',
                'placeholder' : 'Enter the title',


            }
        ),
    )
    content = forms.CharField(
        label = "내용",
        widget = forms.Textarea(
            attrs={
                'class' : 'mt-3 fw-bold',
                'placeholder' : 'Enter the content',
                'rows':5, # 들어가는 글자수가 아니라 텍스트박스 크기
                'column' : 50, # 텍스트박스 크기
                'maxlength' : 255, # 글자수 제한


            }
        ),
    )



    # 모델폼 사용방법
    class Meta:
        model = Article
        fields = '__all__'