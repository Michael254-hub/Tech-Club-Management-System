from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class CustomUser(User):
    pass #placeholder for future implementation
    #Add custom fields here,e.g.,
    #role = models.CharField(max_length=20, choices=[('member',
    #'Member'), (admin,'Admin')])

class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return self.title

"""class Resource(models.Model):
    name = models.CharField(max_length=255)
    link = models.URLField()
    description = models.TextField()
    file = models.FileField(upload_to="resources/, default.pdf")

    def __str__(self):
        return self.name"""

class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)
    content = models.TextField()

    def __str__(self):
        return self.title

class CommunityPost(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)
    content = models.TextField()

    def __str__(self):
        return self.title

class ContactMessage(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name}"

class Member(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)