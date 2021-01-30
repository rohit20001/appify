from django.urls import path
from . import views

urlpatterns = [
    path('',views.page2,name = "page2"),
]
