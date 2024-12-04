from django.db import models

# Create your models here.

class Resource(models.Model):
    name = models.CharField(max_length=255)
    link = models.URLField()
    description = models.TextField()

    def __str__(self):
        return self.name

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