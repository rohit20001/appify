from django.urls import path
from . import views

urlpatterns = [
    path('', views.page1, name="page1"),
    path('blog/', views.blog, name="blog"),
    path('page1/', views.page1, name="page1"),
    path('projects/', views.projects, name="projects"),
    path('page2/', views.page2, name="page2"),
    path('courses/', views.courses, name="courses"),
]
