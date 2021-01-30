from django.shortcuts import render

# Create your views here.
def page1(request):
    return render(request,"tmp/page1.html",)

def blog(request):
    context = {
        "data": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        "trend": [1, 2, 3],
    }
    return render(request,"tmp/blog.html",context)



def projects(request):
    context = {
        "data": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        "trend": [1,2,3],
    }
    # return response
    return render(request,"tmp/projects.html",context)