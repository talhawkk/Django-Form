from django import forms
class Admissions(forms.Form):
    name=forms.CharField()
    age=forms.IntegerField()
    username=forms.CharField()
    email=forms.EmailField()
    
