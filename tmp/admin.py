from django.contrib import admin
from tmp.models import Post,Project,New_Student,extendedUser,Course,Paid_Student,Story
from django.contrib.auth.models import User

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'content_upper_para','content_lower_para', 'posted_date','postedBy')

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('head', 'content', 'posted_date_project','postedBy_project')

class New_StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'contact','dob','sub','When_contacted')

class extendedUserAdmin(admin.ModelAdmin):
    list_display = ('phone','email')

class CourseAdmin(admin.ModelAdmin):
    list_display = ('course_name','course_image','course_teacher','Features_of_courses','posted_date','fees','aboutTeacher')

class Paid_StudentAdmin(admin.ModelAdmin):
    list_display = ('username','name','course_name','course','amount','payment_id','paid','purchased_date')

class StoryAdmin(admin.ModelAdmin):
    list_display = ('story_image','brief_content','story_by')





admin.site.register(Post, PostAdmin)
admin.site.register(Project,ProjectAdmin)
admin.site.register(New_Student,New_StudentAdmin)
admin.site.register(extendedUser,extendedUserAdmin)
admin.site.register(Course,CourseAdmin)
admin.site.register(Paid_Student,Paid_StudentAdmin)
admin.site.register(Story,StoryAdmin)