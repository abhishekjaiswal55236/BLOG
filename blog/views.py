from django.shortcuts import render,get_object_or_404
from .models import Post,Topic
# Create your views here.





def home(request):
    topic = Topic.objects.get(pk=1)
    post_topic1 = Post.objects.filter(topic = topic)
    all_topics = Topic.objects.all()
    return render(request,'blog/home.html',{'topic':topic,'posts':post_topic1,'all_topics':all_topics})



def posts(request , topic_id):
    this_topic = Topic.objects.get(pk=topic_id)
    posts = Post.objects.filter(topic = this_topic)
    all_topics = Topic.objects.all()
    return render(request,'blog/home.html',{'posts':posts,'topic':this_topic,'all_topics':all_topics})


def post(request,topic_id,post_id):
    this_topic = Topic.objects.get(pk=topic_id)
    post = Post.objects.get(pk=post_id)
    all_topics = Topic.objects.all()
    return render(request,'blog/post.html',{'topic':this_topic,'post':post,'all_topics':all_topics})

def contact(request):
    all_topics = Topic.objects.all()

    return render(request,'blog/contact.html',{'all_topics':all_topics})

def about(request):
    all_topics = Topic.objects.all()

    return render(request,'blog/about.html',{'all_topics':all_topics})
