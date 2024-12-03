from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def Machine_learning(request):
    offering = {'what' : 'lots of free & paid'}
    return render(request,'machine_learning/ml.html', context=offering)

def dtree(request):
    return render(request,'machine_learning/DT.html')


def K_nearest(request):
    offering = {'name' : 'TANZIM HASAN RIZBI','versity' : 'INTERNATION ISLAMIC UNIVERSITY CHITTAGONG'}
    return render(request,'machine_learning/knn.html',context=offering)

def random(request):
    return render(request,'machine_learning/random_forest.html')
