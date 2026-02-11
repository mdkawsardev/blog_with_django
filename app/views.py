from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from .models import Post
import os
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
    data = Post.objects.get(unique_code=unique_code)
    if request.method == "POST":
        if len(request.FILES) != 0:
            if len(data.banner) > 0:
                os.remove(data.banner.path)
            data.banner = request.FILES['banner']
        data.title = request.POST.get['title']
        data.description = request.POST.get['description']
        data.save()
    context = {
        'blogs': Post.objects.filter(unique_code=unique_code).all()
    }
    return render(request, 'details.html', context)

def category(request):
    return HttpResponse("I'm done")

def analyze(request):
    if request.method == "GET":
        texts = request.GET.get('texts')
        checkbox = request.GET.get('checkme', 'off')
        punch = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        value = ""
        # This operation is to remove punctuation marks from texts
        if checkbox == "on":
            for text in texts:
                if text not in punch:
                    value+= text
    return render(request, 'analyze.html', {'text':value})

def edit(request):
    pass