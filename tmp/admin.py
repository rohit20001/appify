from django.contrib import admin
from tmp.models import Post,Project

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'content_upper_para','content_lower_para', 'posted_date','postedBy')

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('head', 'content', 'posted_date_project','postedBy_project')

admin.site.register(Post, PostAdmin)
admin.site.register(Project,ProjectAdmin)