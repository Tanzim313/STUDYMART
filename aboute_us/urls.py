from django.urls import path
from . import views
 
 
urlpatterns = [
    path('au/',views.aboute_us),
    path('t/',views.teachers_info)

]
