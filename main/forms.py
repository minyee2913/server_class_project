from django import forms
from .models import ProblemSet, Problem

class ProblemSetForm(forms.ModelForm):
    default_total_score = forms.IntegerField(required=False, initial=100, label="총점")
    total_problems = forms.IntegerField(required=False, initial=20, label='문제 수')
    class Meta:
        model = ProblemSet
        fields = ['name', 'default_total_score', 'total_problems', 'total_score']
        labels = {
            'name': '문제 세트 이름',
        }
        widgets = {
            'default_total_score': forms.NumberInput(attrs={'value': 0}),
            'total_problems': forms.NumberInput(attrs={'value': 0}),
        }
        exclude = ['total_score']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        instance = super().save(commit=False)
        # default_total_score 값을 total_score에 대입
        instance.total_score = instance.default_total_score
        if commit:
            instance.save()
        return instance

class ProblemForm(forms.ModelForm):
    class Meta:
        model = Problem
        fields = ['score', 'success', 'question_text']
        labels = {
            'score': '점수',       # 점수
            'success': '성공 여부',  # 성공 여부
            'question_text': '문제 내용',  # 문제 내용
        }

    question_text = forms.CharField(required=False, widget=forms.Textarea(attrs={'placeholder': '질문을 입력해주세요 (선택 사항)'}))
