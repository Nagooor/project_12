from django.shortcuts import render

# Create your views here.
def ssmb(request):
    return render(request,'ssmb.html')

def ntr(request):
    return render(request,'ntr.html')