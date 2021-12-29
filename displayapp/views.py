from django.shortcuts import render
from displayapp.models import Student_Data
# Create your views here.

def insert_display(request):
    for i in range(3):
        usn=input('Enter the usn : ')
        name=input('Enter the name : ')
        age=int(input('Enter the age : '))  
        gender=input('Enter the gender : ')
        course=input('Enter the course : ')
        
        student_data=Student_Data.objects.create(usn=usn,name=name,age=age,gender=gender,course=course)
        student_data.save()

    return render(request,'displayapp/inserting.html')
        
