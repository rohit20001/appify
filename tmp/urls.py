from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.page1, name="page1"),
    path('blog/', views.blog, name="blog"),
    path('page1/', views.page1, name="page1"),
    path('page2/', views.page2, name="page2"),
    path('courses/', views.courses, name="courses"),
    path('blog/post/<int:post_id>/', views.post, name="post"),
    path('projects/',views.projects,name="projects"),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
