from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
<<<<<<< HEAD
    path('', views.page1, name="page1"),
    path('blog/', views.blog, name="blog"),
    path('page1/', views.page1, name="page1"),
    path('projects/', views.projects, name="projects"),
    path('page2/', views.page2, name="page2"),
    path('courses/', views.courses, name="courses"),
]
=======
    path('',views.page1,name = "page1"),
    path('blog/',views.blog,name = "blog"),
    path('blog/post/<int:post_id>/', views.post, name="post"),
    path('page1/',views.page1,name = "page1"),
    path('projects/',views.projects,name="projects"),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
>>>>>>> d592c596a4ba7187f5a6f5a7f307e7bbb6399d45
