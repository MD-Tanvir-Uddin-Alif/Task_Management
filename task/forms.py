from django import forms
from .models import Task

class Add_Task(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'

        widgets = {
            'assigned_date': forms.DateInput(attrs={'type': 'date'}),
            'category': forms.CheckboxSelectMultiple,
        }