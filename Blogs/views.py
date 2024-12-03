from django.http import HttpResponse
from django.shortcuts import render
from . forms import TeacherRegistration



# Create your views here.

def blog1(request):
    offering = {'name' : 'TANZIM HASAN RIZBI','pos' : 'BACKEND DEVELOPER😀 ❤️','study' : 'B.S.C IN COMPUTER SCIENCE AND ENGINEERING'}
    return render(request,'Blogs/blogs.html',context=offering)

def showformdata(request):
    
    if request.method == 'POST':
        fm = TeacherRegistration(request.POST)
        print(fm)
        print('This is POST statement')
        print(fm.cleaned_data)
    else:
        fm = TeacherRegistration()
        print('This is GET statement')

    return render(request,'Blogs/forms.html',{'form':fm})
