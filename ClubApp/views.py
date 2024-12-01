from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contacts.html')

def blog(request):
    return render(request, 'blog.html')

def programs(request):
    return render(request, 'programs.html')

def community(request):
    return render(request, 'community.html')

def resources(request):
    return render(request, 'resources.html')