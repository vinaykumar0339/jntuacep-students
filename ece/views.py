from django.shortcuts import render

# Create your views here.
def ece(request):
    return render(request,'branches/ece/ece.html')