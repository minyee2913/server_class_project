from django import forms
from .models import ProblemSet, Problem

class ProblemSetForm(forms.ModelForm):
    class Meta:
        model = ProblemSet
        fields = ['name']

class ProblemForm(forms.ModelForm):
    class Meta:
        model = Problem
        fields = ['order', 'score', 'success', 'question_text']
