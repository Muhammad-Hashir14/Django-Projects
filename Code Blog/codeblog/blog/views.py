from django.shortcuts import render, HttpResponse
from .models import Post

# Create your views here.
def blog(request):
    allposts = Post.objects.all()
    context = {"allposts": allposts}
    return render(request, "blogs/blog.html", context)

def blogpost(request, slug):
    post = Post.objects.filter(slug=slug).first()
    postblog = {"post": post}
    return render(request, "blogs/blogpost.html", postblog)