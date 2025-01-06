from django import forms
class Admissions(forms.Form):
    name=forms.CharField()
    age=forms.IntegerField()
    username=forms.CharField()
    email=forms.EmailField()
    password=forms.CharField(widget=forms.PasswordInput())
    Rd=forms.CharField(widget=forms.PasswordInput())
    def clean(self):
        cleaned_data= super().clean()
        valp=cleaned_data['password']
        vale=cleaned_data['Rd']

        if valp!=vale:

            raise forms.ValidationError("Password Does Not match")