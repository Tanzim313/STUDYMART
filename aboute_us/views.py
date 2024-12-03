from django.http import HttpResponse
from django.shortcuts import render
from aboute_us.models import Teacher

# Create your views here.
def aboute_us(request):
    return render(request,'aboute/au.html')


def teachers_info(request):
    teach = Teacher.objects.all()
    
    return render(request,'aboute/t.html',{'thr':teach})
