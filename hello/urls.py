from django.urls import path
from . import views

urlpatterns=[
    path("",views.index,name="index"),
    path("Saad/",views.saad,name="Saad"),
    path("<str:name>",views.greet,name="greet"),
]