from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from taggit.managers import TaggableManager

STATUS = (
    (0,"Draft"),
    (1,'Publish')
)

class Topic(models.Model):
    heading = models.CharField(max_length=200,unique=True)
    description = models.CharField(max_length=300)
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='blog_topics')
    created_on = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to = 'images/',default='')
    class Meta:
        ordering = ['-created_on']
    def __str__(self):
        return self.heading

class Post(models.Model):

    image = models.ImageField(upload_to = 'images/',default='')
    description = models.CharField(max_length=300,default = '')
    topic = models.ForeignKey(Topic,on_delete=models.CASCADE,related_name='topic_posts')
    title = models.CharField(max_length=200,unique=True)
    slug = models.SlugField(max_length=200,unique=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices = STATUS , default = 0)
    tag = TaggableManager()


    class Meta:
        ordering = ['-updated_on']

    def __str__(self):
        return self.title
