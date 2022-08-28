from distutils.debug import DEBUG
from pyexpat import model
from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.conf import settings

CATEGORIES = [
    ('football', 'Football'),
    ('badminton', 'Badminton'),
    ('swimming', 'Swimming'),
    ('basketball', 'Basketball'),
    ('volleyball', 'Volleyball'),
    ('table-tennis', 'Table Tennis')

]

class PostManager(models.Manager):
    def like_toggle(self, user, post_obj):
        if user in post_obj.liked.all():
            is_liked = False
            post_obj.liked.remove(user)
        else:
            is_liked = True
            post_obj.liked.add(user)
        return is_liked


class Post(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    video_link = models.TextField(blank=True, null=True)
    liked = models.ManyToManyField(
        settings.AUTH_USER_MODEL, blank=True, related_name='liked')
    date_posted = models.DateTimeField(default=timezone.now)
    # choose multiple categories
    category = models.CharField(max_length=20, choices=CATEGORIES ,default='football')
    objects = PostManager()

    class Meta:
        ordering = ('-date_posted', )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.pk})


class Comment(models.Model):
    post = models.ForeignKey(
        Post, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=True)

    def approve(self):
        self.approved_comment = True
        self.save()

    def get_absolute_url(self):
        return reverse("post_list")

    def __str__(self):
        return self.author.username

# Create model for subscribers for the user to subscribe 
class Subscriber(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_subscribed = models.DateTimeField(default=timezone.now)

    subscribers = models.ManyToManyField(
        settings.AUTH_USER_MODEL, blank=True, related_name='subscribers')

    def __str__(self):
        return self.user.username


class News(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='images/', blank=False, null=False, default='images/default.jpg')
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, blank=True, null=True
        )
    date_posted = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('index')

