
from django.urls import path 
from . import views

urlpatterns= [
    
    path("", views.index, name="index_name"),
    path("<int:dooro>", views.choose_num),
    path("<str:dooro>", views.choose, name="saxaha")
   
 

]