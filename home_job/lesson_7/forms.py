from django import forms
from lesson_7.models import ModelPersonTask3


class ReviewForTask1(forms.Form):
    email = forms.EmailField()
    description = forms.Textarea()
    grade = forms.ChoiceField(
        choices=[('bad', 'bad'), ('normal', 'normal'), ('good', 'good')])
    relation = forms.ChoiceField(
        choices=[('positive', 'positive'), ('negative', 'negative')])
    phone = forms.CharField()


class AuthorizationForTask2(forms.Form):
    email = forms.EmailField()
    login = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())


class FormFromModelTask3(forms.ModelForm):
    class Meta:
        model = ModelPersonTask3
        fields = '__all__'
