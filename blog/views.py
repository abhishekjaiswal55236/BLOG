from django.shortcuts import render,get_object_or_404
from .models import Post,Topic
# Create your views here.





def home(request):
    topics = Topic.objects.all
    return render(request,'blog/home.html',{'topics':topics})



def posts(request , topic_id):
    this_topic = Topic.objects.get(pk=topic_id)
    posts = Post.objects.filter(topic = this_topic)

    return render(request,'blog/posts.html',{'posts':posts,'topic':this_topic})


def post(request,topic_id,post_id):
    this_topic = Topic.objects.get(pk=topic_id)
    post = Post.objects.get(pk=post_id)
    return render(request,'blog/post.html',{'topic':this_topic,'post':post})
