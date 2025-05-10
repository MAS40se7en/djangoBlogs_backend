from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify
from django.utils import timezone
from django.conf import settings
# Create your models here.

class CustomUser(AbstractUser):
    bio = models.TextField(null=True, blank=True)
    job_title = models.CharField(max_length=100, null=True, blank=True)
    profile_image = models.ImageField(upload_to='profile_img', null=True, blank=True)
    facebook = models.URLField(max_length=255, blank=True, null=True)
    twitter = models.URLField(max_length=255, blank=True, null=True)
    instagram = models.URLField(max_length=255, blank=True, null=True)
    youtube = models.URLField(max_length=255, blank=True, null=True)
    github = models.URLField(max_length=255, blank=True, null=True)
    
    def __str__(self):
        return self.username

class Blog(models.Model):
    
    CATEGORY = (("Technology", "Technology"), ("Business", "Business"), ("Politics", "Politics"), ("Entertainment", "Entertainment"), ("Economy", "Economy"), ("Lifestyle", "Lifestyle"), ("Web Development", "Web Development"))
    
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    content = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, related_name='blogs', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(null=True, blank=True)
    is_draft = models.BooleanField(default=True)
    category = models.CharField(max_length=255, choices=CATEGORY, null=True)
    featured_image = models.ImageField(upload_to='blog_img', null=True, blank=True)
    
    class Meta:
        ordering = [
            "-published_at"
        ]
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        base_slug = slugify(self.title)
        slug = base_slug
        num = 1
        while Blog.objects.filter(slug=slug).exists():
            slug = f"{base_slug}-{num}"
            num += 1
        self.slug = slug
        
        if not self.is_draft and self.published_at is None:
            self.published_at = timezone.now()
            
        super().save(*args, **kwargs)