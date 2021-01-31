from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator
from tmp.models import Post

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

    context = {'page_obj': page_obj}
    return render(request,"tmp/blog.html",context)

def post(request, post_id=None):
    post = get_object_or_404(Post, id=post_id)
    x = Post.objects.all().order_by('-posted_date')
    context = {'post': post,'x': x}
    return render(request, 'tmp/post.html', context)



def projects(request):
    context = {
        "data": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        "trend": [1,2,3],
    }
    # return response
    return render(request,"tmp/projects.html",context)