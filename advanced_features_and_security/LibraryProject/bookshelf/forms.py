from django import forms

class ExampleForm(forms.Form):
    title = forms.CharField(max_length=255)
    year = forms.DateField()