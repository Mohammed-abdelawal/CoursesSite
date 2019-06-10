from django.contrib import admin
from .models import Profile , Courses, Video, User_Course, Post
# Register your models here.

admin.site.register(Profile)
admin.site.register(User_Course)

class PostAdmin(admin.ModelAdmin): 
    model = Post
    list_display = ('__str__','Type')

class VideoInline(admin.StackedInline):
    model = Video
    extra =1


class CoursesAdmin(admin.ModelAdmin): 
    inlines = [VideoInline]

admin.site.register(Courses,CoursesAdmin)
admin.site.register(Post ,PostAdmin)
