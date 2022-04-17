from django import forms
from django.shortcuts import redirect, render
from .import models
from .import forms
from django.http import request


# Create your views here.
def creating(request):
    obj=forms.bookform()
    if request.method=='POST':
        obj=forms.bookform(request.POST)
        if obj.is_valid():
            obj.save()
            obj=forms.bookform()
            return redirect("/home/list")
    return render(request,"create.html",{"order":obj})   

def listing(request)    :
    obj=models.bookmodel.objects.all()
    return render(request,"homelisting.html",{"key":obj})

def reading(request,pk):
    obj=models.bookmodel.objects.get(id=pk)    
    return render(request,"read.html",{"key":obj})


def updating(request,pk):
    bobj=models.bookmodel.objects.get(id=pk)    
    obj=forms.bookform(instance=bobj)
    if request.method=='POST':
        obj=forms.bookform(request.POST,instance=bobj)
        if obj.is_valid():
            obj.save()
            return redirect("/home/list")
    return render(request,"create.html",{"order":obj})      

def deleting(request,pk):
    obj=models.bookmodel.objects.get(id=pk)
    if request.method=='POST':
        models.bookmodel.delete(obj)
        return redirect("/home/list")
    return render(request,"delete.html",{"item":obj})