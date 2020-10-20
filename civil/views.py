from django.shortcuts import render

# Create your views here.
def civil(request):
    return render(request,'branches/civil/civil.html')