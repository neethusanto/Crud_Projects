from .models import Task
from django import forms

class CrudForm(forms.ModelForm):
    class Meta:
        model=Task
        fields=['slno','name','description']