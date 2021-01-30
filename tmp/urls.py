from django.urls import path
from . import views

urlpatterns = [
    path('', views.page1, name="page1"),
    path('blog/', views.blog, name="blog"),
    path('page1/', views.page1, name="page1"),
    path('projects/', views.projects, name="projects"),
]
