from django.shortcuts import render, HttpResponse
from .models import Contact
from django.contrib import messages
from blog.models import Post
# Create your views here.

def home(request):
    return render(request, "home/home.html")
    
def about(request):
    return render(request, "home/about.html")

def contact(request):
    messages.success(request, "Welcome to Contact Page")
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']
        if len(name) <2 or len(email) < 5 or len(phone) < 10 or len(content) <5:
            messages.error(request, "Please fill form correctly")
        else:
            contact = Contact(name=name, email = email, phone = phone, content = content)
            contact.save()
            messages.success(request, "Message sent successfully!")
    return render(request, "home/contact.html")

def search(request):
    query = request.GET["query"]
    allPosts = Post.objects.filter(title__icontains=query)
    context = {"allPosts":allPosts}
    return render(request, "home/search.html", context)