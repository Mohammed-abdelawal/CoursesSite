from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    ''' this class is model to store more efficient data about our users 
        - it connect with django user model with (user_id)
     '''
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    about = models.TextField(null=True,max_length=2000)
    phone = models.CharField(max_length=12)
    is_Male = models.BooleanField(name='Gender',choices=((False,'Male') , (True,'Female')) )
    birthdate = models.DateField()
    country = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)

    def __str__(self):
        return self.user_id.__str__()


class Courses(models.Model):
    title = models.CharField(max_length=150)
    field = models.IntegerField(choices = ( (0,'Mobile Development') ,
                                         (1,'Web Development') ,
                                         (2,'Web Design') ,
                                         (3,'Enterprise'),
                                         (4,'Financial Learning'),
                                         (5,'Basic Programming') ) )
    description = models.TextField()
    intro_video = models.URLField(verbose_name='introduction video', help_text='youtube link')
    price = models.FloatField(default=0.0,help_text='with dollars $')
    rating = models.FloatField(editable=False,default=0.0)
    videos_num = models.IntegerField()
    videos_Time = models.IntegerField(verbose_name='total videos Time', help_text=' in minutes')

    def __str__(self):
        return self.title


class Video(models.Model):
    course = models.ForeignKey(Courses,on_delete = models.CASCADE)
    name = models.CharField(max_length=80)
    host = models.IntegerField(choices = ( (0,'You Tube'),
                                           (1,'Vimeo'),
                                           (2,'Dailymotion'),
                                           (3,'Jetpack'),
                                           (4,'Wistia'),
                                           (5,'Vidyard')    ))
    video_link = models.URLField()
    desc = models.TextField(verbose_name='Description')
    attachment = models.FileField(upload_to='lessons/', null=True, blank = True)
    link1 = models.URLField(null=True, blank = True)
    link_String1 = models.CharField(max_length=50,null=True, blank = True)
    link2 = models.URLField(null=True, blank = True)
    link_String2 = models.CharField(max_length=50,null=True, blank = True)

    def __str__(self):
        return self.name


class User_Course(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    is_enroll = models.BooleanField(default=False)
    paid = models.FloatField(default=0.0)
    Progrss = models.IntegerField()
    review_num = models.FloatField()
    review = models.TextField()


class Post(models.Model):
    course = models.ForeignKey( Courses, on_delete = models.CASCADE)
    text = models.TextField()
    pic = models.ImageField(upload_to = 'post_pic/', default = None, blank = True)
    attachment = models.FileField(upload_to='post_doc/', default = None, blank = True)
    replay_to = models.OneToOneField(to='Post' ,on_delete=models.CASCADE, null = True,blank=True)
    
    def Type(self):
        if self.replay_to == None:
            return 'Post'
        return 'Comment'

    def __str__(self):
        return  self.text
    