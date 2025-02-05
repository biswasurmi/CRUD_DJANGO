from django import forms
from .models import students

class StudentForm(forms.ModelForm):
    class Meta:
        model = students
        fields = ['name', 'email', 'course', 'address', 'phone']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'required': 'required'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'required': 'required'}),
            'course': forms.TextInput(attrs={'class': 'form-control', 'required': 'required'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'required': 'required'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'required': 'required'}),
        }
