from django import forms
from .models import cartoon


class CartoonForm(forms.ModelForm):
    class Meta: 
        model = cartoon
        fields = '__all__'