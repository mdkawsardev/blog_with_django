from django.shortcuts import render, redirect
from django.contrib import messages
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

def details(request, pk):
    context = {
        'blogs': Post.objects.filter(id=pk).all()
    }
    return render(request, 'details.html', context)