from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from .models import Post
# Create your views here.
def index(request):
    return render(request, 'index.html')

def blog(request):
    context = {
        'blogs': Post.objects.all()
    }
    return render(request, 'blog.html', context)

def post(request):
    if request.method == "POST":
        title = request.POST['title']
        banner = request.FILES['banner']
        description = request.POST['description']
        Post.objects.create(
            title=title,
            banner=banner,
            description=description
        )
        messages.success(request, 'Post uploaded successfully!')
        return redirect('post')
    return render(request, 'post.html')

def details(request, unique_code):
    context = {
        'blogs': Post.objects.filter(unique_code=unique_code).all()
    }
    return render(request, 'details.html', context)

def category(request):
    return HttpResponse("I'm done")