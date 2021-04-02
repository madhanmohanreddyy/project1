from django.shortcuts import render

# Create your views here.
def linde(request):
    d={'name':'madhan mohan reddy','attitude':'intelligent'}
    return render(request,'hai.html',context=d)