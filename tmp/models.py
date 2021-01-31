from django.db import models
from ckeditor.fields import RichTextField


class Post(models.Model):
    title = models.CharField(max_length=100)
    content_upper_para = RichTextField()
    content_lower_para = RichTextField(default="")
    posted_date = models.DateTimeField(auto_now_add=True)
    postedBy = models.CharField(max_length=50)
    blogImage = models.ImageField(upload_to="blog/images",default="")
    authorImage = models.ImageField(upload_to="author/images",default="")
    aboutAuthor = models.CharField(max_length=1000,default="")

class Project(models.Model):
    head = models.CharField(max_length=100)
    content = RichTextField(max_length=5000)
    posted_date_project = models.DateTimeField(auto_now_add=True)
    postedBy_project = models.CharField(max_length=50)
    projectImage = models.ImageField(upload_to="blog/images",default="")
# Create your models here.
