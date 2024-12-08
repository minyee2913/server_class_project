# forms.py
from django import forms
from .models import ProblemSet, Problem

class ProblemSetForm(forms.ModelForm):
    class Meta:
        model = ProblemSet
        fields = ['name']

class ProblemForm(forms.ModelForm):
    class Meta:
        model = Problem
        fields = ['question_text', 'score', 'success']
        widgets = {
            'question_text': forms.Textarea(attrs={'rows': 3, 'cols': 50}),
        }
