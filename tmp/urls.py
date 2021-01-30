from django.urls import path
from . import views

urlpatterns = [
    path('',views.page2,name = "page2"),
    path('page1/',views.page1,name = "page1"),
]
