from django.shortcuts import render
from django import forms

tasks= ["foo", "bar", "baz"]
# Create your views here.

class NewTaskForm(forms.Form):
    task=forms.CharField(label="New Task")
    priority=forms.IntegerField(label="Priority",min_value=1,max_value=10)
    
def index(request):
    return render(request,"tasks/index.html",{
        "tasks":tasks
    })

def add(request):
    if request.method=="POST":
        form=NewTaskForm(request.POST)
        if form.is_valid():
            task=form.cleaned_data["task"]
            priority=form.cleaned_data["priority"]
            tasks.append(task)
            return render(request,"tasks/index.html",{
                "tasks":tasks
            })
        else:
            return render(request,"tasks/add.html",{
                "form":form
            })
    # if the request method is GET, we display the form
    return render (request,"tasks/add.html",{
        "form":NewTaskForm()
    })