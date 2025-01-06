from django import forms
class Admissions(forms.Form):
    name=forms.CharField()
    age=forms.IntegerField()
    username=forms.CharField()
    email=forms.EmailField()
    password=forms.CharField(widget=forms.PasswordInput())
    # Upload_CV=forms.CharField(widget=forms.FileInput(), required=False)
    
