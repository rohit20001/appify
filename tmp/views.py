from django.shortcuts import render

# Create your views here.

def page2(request):
    return render(request,"tmp/page2.html",)

def page1(request):
    return render(request,"tmp/page1.html",)

def blog(request):
    return render(request,"tmp/blog.html",)