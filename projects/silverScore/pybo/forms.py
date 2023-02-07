from django import forms
from pybo.models import Question
from django import forms
from pybo.models import Question

class QuestionForm(forms.ModelForm):    # 외부 클래스
    class Meta:     # 내부 클래스
        model = Question  # 사용할 모델
        fields = ['subject', 'content']  # QuestionForm에서 사용할 Question 모델의 속성
        widgets = {
            'subject': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),
        }
        labels = {
            'subject': '제목',
            'content': '내용',
        }