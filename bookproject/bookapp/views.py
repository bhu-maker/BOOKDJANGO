from django import forms
from django.shortcuts import redirect, render
from .import models
from .import forms
from django.http import request
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .serializers import bookser



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

@api_view(['GET'])
def gettingall(request):
    modvar=models.bookmodel.objects.all()
    servar=bookser(modvar,many=True)
    return Response(servar.data)

@api_view(['POST'])    
def postting(request):
    servar=bookser(data=request.data)
    if servar.is_valid():
        servar.save()
        return Response(servar.data,status=status.HTTP_201_CREATED)

@api_view(['GET'])        
def readgetting(request,pk):
    modvar=models.bookmodel.objects.get(title=pk)
    servar=bookser(modvar)
    return Response(servar.data,status=status.HTTP_200_OK)


    