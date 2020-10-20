from django.shortcuts import render

# Create your views here.
def mech(request):
    return render(request,'branches/mech/mech.html')

def R_15(request):
    return render(request,'branches/mech/r_15.html')

def R_19(request):
    return render(request,'branches/mech/r_19.html')

def R_15_firstyear(request,year):
    pass