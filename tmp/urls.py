from django.urls import path
from tmp import views

urlpatterns = [
    path('', views.page1, name="page1"),
]