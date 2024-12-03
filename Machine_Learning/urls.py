from django.urls import path
from . import views


urlpatterns = [
    
    path('m/',views.Machine_learning),
    path('DT/',views.dtree),
    path('k/',views.K_nearest),
    path('rn/',views.random),
    
]

