from django import forms
from .models import Questionnaire

class QuestionnaireForm(forms.ModelForm):
    class Meta:
        model = Questionnaire
        fields = ['question1', 'question2', 'question3', 'question4', 'question5']
        widgets = {
            'question1': forms.Textarea(attrs={'rows': 3}),
            'question2': forms.Textarea(attrs={'rows': 3}),
            'question3': forms.Textarea(attrs={'rows': 3}),
            'question4': forms.Textarea(attrs={'rows': 3}),
            'question5': forms.Textarea(attrs={'rows': 3}),
        }

