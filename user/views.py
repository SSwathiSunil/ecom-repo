from django.shortcuts import render

# Create your views here.
def Index(request):
    return render(request,'index.html')

def New(request):
    return render(request,'new1.html')
