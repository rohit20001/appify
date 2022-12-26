from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.page1, name="page1"),
    path('blog/', views.blog, name="blog"),
    path('home/', views.page1, name="page1"),
    path('story/', views.page2, name="page2"),
    path('courses/', views.courses, name="courses"),
    path('blog/post/<int:post_id>/', views.post, name="post"),
    path('courses/subject/<int:post_id>/', views.subject, name="subject"),
    path('projects/',views.projects,name="projects"),
    path('signup/', views.signup, name="signup"),
    path('login/', views.login, name="login"),
    path('logout/',views.logout_view,name ="logout"),
    path('aboutus/',views.aboutus,name ="aboutus"),
    path('profile/',views.profile,name ="profile"),
    path('success/',views.success,name ="success"),
    path('confirm/',views.confirm,name ="confirm"),
    # path('send_mail/',send_gmail,name= "send_mail")
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
