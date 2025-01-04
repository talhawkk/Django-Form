from django.shortcuts import render
from home.models import Student
from home.form import Admissions
# Create your views here.
def home(request):
    stud=Student.objects.all()
    forms=Admissions(auto_id=True, label_suffix="->")
    return render(request,'home/home.html',{'stu':stud,'form':forms})
