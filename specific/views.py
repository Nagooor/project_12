from django.shortcuts import render

#Create your views here.
def pspk(request):
    return render(request,'pspk.html')

def rc(request):
    return render(request,'rc.html')