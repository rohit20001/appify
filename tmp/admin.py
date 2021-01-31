from django.contrib import admin
from tmp.models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'content_upper_para','content_lower_para', 'posted_date','postedBy')

admin.site.register(Post, PostAdmin)