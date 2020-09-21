from django.shortcuts import render, get_object_or_404
from .models import Post
# Create your views here.

def list(request):
    posts = Post.objects
    return render(request,'list.html', {'posts':posts})

def post_detail(request, post_id):
    post_detail = get_object_or_404(Post, pk=post_id)
    return render(request, 'detail.html', {'post': post_detail})

# def post_detail(request, post_id):
#     post_detail = get_object_or_404(post_models.Post, pk=post_id)
#     try:
#         is_scraped = request.user.scraped.filter(pk=post_id).exists()
#     except:
#         is_scraped = ""

#     if request.method == "POST":
#         form = CommentForm(request.POST, request.FILES)
#         if form.is_valid():
#             comment = form.save(commit=False)
#             comment.post = post_detail
#             comment.user = request.user
#             comment.save()
#             return redirect("/post/" + str(post_id))
#     else:
#         form = CommentForm()
#     return render(
#         request,
#         "posts/post_detail.html",
#         {"post_detail": post_detail, "form": form, "is_scraped": is_scraped},
#     )
