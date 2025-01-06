from django.shortcuts import render
from home.models import Student
from home.form import Admissions
# Create your views here.
def home(request):
    if request.method=="POST":
        forms=Admissions(request.POST)
        # print("post se ayi ha")
        # print(forms)
        # print("PPPoost")
        if forms.is_valid():
            print(forms.cleaned_data)
            return render(request,'home/success.html',{'Name':forms.cleaned_data['name']})


    else:
        # stud=Student.objects.all()
        forms=Admissions(auto_id=True, label_suffix="->", initial={'name':'talhawk','email':'@gmail.com'},field_order=['username','email','name','email'])
        print("by get request")
    return render(request,'home/home.html',{'form':forms})
