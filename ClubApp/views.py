from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == 'POST':
        # Process the form submission (example logic)
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        # Here you can handle saving data or sending an email
        return HttpResponse(f"Thank you, {name}! Your message has been received.")
    return render(request, 'contacts.html')


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