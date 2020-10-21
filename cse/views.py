from django.http import request
from django.shortcuts import render
from . import urls
# Create your views here.
def cse(request):
    return render(request,'branches/cse/cse.html')

def display(request):
    return render(request,'branches/cse/DisplayData.html')