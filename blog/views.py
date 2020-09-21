from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm
# Create your views here.

def list(request):
    posts = Post.objects
    return render(request,'list.html', {'posts':posts})

def post_detail(request, post_id):
    post_detail = get_object_or_404(Post, pk=post_id)
    return render(request, 'detail.html', {'post': post_detail})

def write(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect("/blog/")
    
    else:
        form = PostForm()
    return render(request, 'write.html', {"form": form})
