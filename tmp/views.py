from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator
from tmp.models import Post,Project

# Create your views here.
def page1(request):
    return render(request,"tmp/page1.html",)

def page2(request):
    return render(request,"tmp/page2.html",)

def courses(request):
    return render(request,"tmp/courses.html",)

def blog(request):
    posts = Post.objects.all().order_by('-posted_date')
    paginator = Paginator(posts, 4)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    projec = Project.objects.all().order_by('-posted_date_project')

    context = {'page_obj': page_obj,'projec':projec}
    return render(request,"tmp/blog.html",context)

def post(request, post_id=None):
    post = get_object_or_404(Post, id=post_id)
    x = Post.objects.all().order_by('-posted_date')
    projec = Project.objects.all().order_by('-posted_date_project')
    context = {'post': post,'x': x,'projec':projec}
    return render(request, 'tmp/post.html', context)



def projects(request):
    projec = Project.objects.all().order_by('-posted_date_project')
    paginator = Paginator(projec, 1)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    x = Post.objects.all().order_by('-posted_date')
    context = {'page_obj': page_obj,'x': x,}
    # return response
    return render(request,"tmp/projects.html",context)
