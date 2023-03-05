from django import forms
from lesson_10.models import Cityes


class CityesForm(forms.ModelForm):
    class Meta:
        model = Cityes
        fields = '__all__'
