from django.shortcuts import render,get_object_or_404,redirect,HttpResponse
from django.core.paginator import Paginator
from tmp.models import Post,Project
from django.contrib.auth.models import User,auth
from django.contrib.auth import logout, login, authenticate
from django.contrib import messages

# Create your views here.
def page1(request):
    return render(request,"tmp/page1.html",)

def page2(request):
    return render(request,"tmp/page2.html",)
def signup(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        phone = request.POST['phone']

        if password1 == password2:
            if User.objects.filter(username=email).exists():
                messages.info(request, "Email Used")
                return redirect('signup')
            else:
                user = User.objects.create_user(username=email, password=password1, email=email, first_name=first_name,
                                                last_name=last_name)
                user.first_name = first_name
                user.last_name = last_name
                user.email = email
                user.phone = phone
                user.save()
                messages.success(request, " Your Lennisters account has been successfully created")
                return redirect('page1')
        else:
            messages.info(request, "Password doesn't match")
            return redirect('signup')
    else:
        return render(request, "tmp/signup.html")





def login(request):
    if request.method == 'POST':
        email = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=email, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("page1")
        else:
            messages.info(request, "Email or password is incorrect")
            return redirect("login")
    else:
        return render(request, "tmp/login.html")

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

def logout_view(request):
    logout(request)
    messages.success(request,"Successfully Log Out")
    return redirect('/')
