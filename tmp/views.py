from django.shortcuts import render,get_object_or_404,redirect,HttpResponse
from django.core.paginator import Paginator
from tmp.models import Post,Project,New_Student,Course,Paid_Student,Story
from django.contrib.auth.models import User,auth
from django.contrib.auth import logout, login, authenticate
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from .models import extendedUser
from django.contrib.auth.decorators import login_required
import razorpay
from datetime import datetime, timedelta
from django.core.mail import send_mail
# Create your views here.
# user =NULL
# @csrf_exempt
def page1(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        dob = request.POST['dob']
        contact = request.POST['contact']
        sub = request.POST['sub']
        if New_Student.objects.filter(email=email).exists():
                messages.info(request, "This Email is in Use, We will contact you soon! ")
                return redirect('/')
        else:
            new_student = New_Student.objects.create(name=name, email=email, dob=dob, contact=contact,sub=sub)
            new_student.name = name
            new_student.email = email
            new_student.dob = dob
            new_student.contact = contact
            new_student.sub=sub
            new_student.save()
            messages.success(request, " We will contact you soon !! ")
            return redirect('/')
    else:
        # print(request.GET)
        # return redirect('/')
        return render(request,"tmp/page1.html",)

def page2(request):
    story = Story.objects.all()
    paginator = Paginator(story, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    blog = Post.objects.all()[:3]
    context = {'page_obj': page_obj,'blog':blog}
    return render(request,"tmp/page2.html",context)


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
                newExtendUser = extendedUser(phone=phone,email=email)
                user.first_name = first_name
                user.last_name = last_name
                user.email = email
                newExtendUser.phone = phone
                newExtendUser.email = email
                newExtendUser.save()
                user.save()
                messages.success(request, " Your Lennisters account has been successfully created")
                return redirect('/')
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
            return redirect('/')
        else:
            messages.info(request, "Email or password is incorrect")
            return redirect("login")
    else:
        return render(request, "tmp/login.html")

def courses(request):
    courses = Course.objects.all().order_by('-posted_date')
    paginator = Paginator(courses, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    # projec = Project.objects.all().order_by('-posted_date_project')
    context = {'page_obj': page_obj}
    return render(request,"tmp/courses.html",context)

def blog(request):
    if request.method == 'POST':
        name = request.POST['uid1']
        idd = request.POST['uid2']
        comment = request.POST['uid3']
        print(name,idd,comment)

        send_mail(
            "Comment From Blog By:- " + name,
            comment,
            idd,
            ['codution.org@gmail.com'],
            fail_silently = False,

        )
        return redirect('/')
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

# yha s new h sb

def aboutus(request):
    return render(request,"tmp/aboutus.html",)

@login_required(login_url='/login/')
def profile(request):
    # if request.user.is_authenticated:

        # Paid_Student.objects.filter(purchased_date=datetime.now()-timedelta(seconds=2)).update(paid=False)

        current_user = request.user
        datas = extendedUser.objects.filter(email=current_user.email)
        for data in datas:
            if(data.email == current_user.email):
                phone = data.phone
                break
        
        purchased_course = Paid_Student.objects.filter(username=current_user.email, paid=True).order_by('-purchased_date')
        
        # for i in purchased_course:
        #     print(i.purchased_date.now().date())
            
         
        context = {'current_user':current_user,'data':phone,'purchased_course':purchased_course}
        return render(request,"tmp/profile.html",context)

@login_required(login_url='/login/')
def subject(request, post_id=None):
    post = get_object_or_404(Course, id=post_id)
    context = {'post': post}
    if request.method == 'POST':
        name = request.user.first_name + request.user.last_name
        course_name = request.POST.get("course_name")
        course = Course.objects.get(course_name=course_name)
        amount = int(request.POST.get("amount"))*100
        client = razorpay.Client(auth=("rzp_test_Yv7NrCx6FwcyM0", "8OIQ7naHTlTIZQTtztKM83ne"))
        payment = client.order.create({'amount':amount,'currency':'INR','payment_capture':'1'})
        # print(payment)
        paid_student = Paid_Student(username = request.user.email,name=name,course_name=course_name,course=course, amount= int(amount)/100,payment_id=payment['id'])
        paid_student.save()
        context['payment'] = payment
        return render(request,"tmp/subject.html", context)
    
    # x = Course.objects.all().order_by('-posted_date')
    # projec = Project.objects.all().order_by('-posted_date_project')
    return render(request, 'tmp/subject.html', context)

@csrf_exempt
def success(request):
    if request.method == "POST":
        a=request.POST
        order_id = ""
        for key,val in a.items():
            if key == 'razorpay_order_id':
                order_id = val
                break
        print(a)
        context = {'a':a}
        user = Paid_Student.objects.filter(payment_id=order_id).first()
        user.paid = True
        user.save()
        return render(request,"tmp/success.html",context)
    else:
        return redirect('/')

def confirm(request):
    return render(request,"tmp/confirm.html")