from django.db import models
from ckeditor.fields import RichTextField


class Post(models.Model):
    title = models.CharField(max_length=50)
    content_upper_para = RichTextField()
    content_lower_para = RichTextField(default="")
    posted_date = models.DateTimeField(auto_now_add=True)
    postedBy = models.CharField(max_length=20)
    blogImage = models.ImageField(upload_to="blog/images",default="")
    authorImage = models.ImageField(upload_to="author/images",default="")
    aboutAuthor = models.CharField(max_length=100,default="")

# Create your models here.
