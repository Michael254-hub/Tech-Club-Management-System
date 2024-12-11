from django.contrib.auth.models import User
from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render,HttpResponse,redirect
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login as auth_login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    return render(request, 'index.html')

def login(request: WSGIRequest):
    if request.method == 'POST':
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        user = authenticate(request, username=username, password=password1)
        if user is not None:
            auth_login(request, user)
            return redirect('index')
        else:
            return render(request, 'login.html', {'error':'Invalid username or password'})

    return render(request, 'login.html')

def signup(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            return HttpResponse("Your password and confirm password are not Same!!")
        else:

            my_user = User.objects.create_user(uname, email, password1)
            my_user.save()
            return redirect('login')

    return render(request, 'signup.html')

def about(request):
    return render(request, 'about.html')


def programs(request):
    # Static data for now; later, you can fetch from the database

    program_list = [
        {'title': 'Web Development Bootcamp',
         'description': 'Learn the fundamentals of front-end and back-end web development.'},
        {'title': 'AI & Machine Learning Workshop',
         'description': 'Explore the basics of AI and build simple machine learning models.'},
        {'title': 'Cybersecurity Basics',
         'description': 'Understand the principles of securing online systems and data.'},
        {'title': 'UI/UX Design Essentials', 'description': 'Master the art of designing user-friendly interfaces.'},
    ]
    return render(request, 'programs.html')


def resources(request):
    #Static data for now; replace with database model later
    resource_list = [
        {'name': 'Python Documentation', 'link': 'https://docs.python.org/3/',
         'description': 'Official Python documentation.'},
        {'name': 'Django Documentation', 'link': 'https://docs.djangoproject.com/en/stable/',
         'description': 'Comprehensive guide for Django framework.'},
        {'name': 'FreeCodeCamp', 'link': 'https://www.freecodecamp.org/',
         'description': 'Learn coding for free with tutorials and exercises.'},
        {'name': 'MDN Web Docs', 'link': 'https://developer.mozilla.org/',
         'description': 'Resources for HTML, CSS, JavaScript, and more.'},
    ]
    return render(request, 'resources.html')


def events(request):
    event_list = [
        {'title': 'Web Development Bootcamp',
         'description': 'Learn the basics of front-end and back-end web development.'},
        {'title': 'AI & Machine Learning Workshop',
         'description': 'Explore the basics of AI and build simple machine learning models.'},
        {'title': 'Cybersecurity Basics',
         'description': 'Understand the principles of securing online systems and data.'},
    ]
    return render(request, 'events.html')

def blog(request):
    # Static data for now; replace with database model later
    blog_posts = [
        {
            'title': '10 Tips for Learning Django',
            'author': 'John Doe',
            'date': '2024-12-01',
            'content': 'Django is a powerful web framework. Here are 10 tips to get started...',
        },
        {
            'title': 'Why Python is Perfect for Web Development',
            'author': 'Jane Smith',
            'date': '2024-11-25',
            'content': 'Python is versatile, readable, and has a strong ecosystem...',
        },
        {
            'title': 'Introduction to REST APIs',
            'author': 'Alex Brown',
            'date': '2024-11-15',
            'content': 'REST APIs are the backbone of modern web development. Learn how to build them...',
            },
    ]
    return render(request, 'blog.html', {'posts': blog_posts})


def community(request):
    # Static data for now; replace with a database later
    community_posts = [
        {
            'title': 'Weekly Tech Talk: Python Basics',
            'author': 'Jane Doe',
            'date': '2024-12-01',
            'content': 'Join our weekly tech talk to discuss Python fundamentals and share tips.',
        },
        {
            'title': 'Hackathon Announcement',
            'author': 'Tech Club Team',
            'date': '2024-11-27',
            'content': 'Participate in our upcoming hackathon and win exciting prizes!',
        },
        {
            'title': 'Volunteers Needed for Coding Bootcamp',
            'author': 'John Smith',
            'date': '2024-11-20',
            'content': 'We’re looking for volunteers to assist in our beginner-friendly coding bootcamp.',
        },
    ]
    return render(request, 'community.html')

def contacts(request):
    if request.method == 'POST':
        # Process the form submission (example logic)
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        # Here you can handle saving data or sending an email
        return HttpResponse(f"Thank you, {name}! Your message has been received.")

    return render(request, 'contacts.html')

def logout(request: WSGIRequest):
    logout(request)
    return redirect('login')