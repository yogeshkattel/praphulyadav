# import timezone
from django.utils import timezone
from .models import Post, Notification
def post_schedule():
    print("post_schedule")
    posts = Post.objects.filter(is_published=False).all()
    for post in posts:
        # check the date and hour minute of the post and compare with the current time
        print(post.schedule_time.date() , timezone.now().date() , post.schedule_time.hour == timezone.now().hour , post.schedule_time.minute , timezone.now().minute) 
        if post.schedule_time.date() == timezone.now().date() and post.schedule_time.hour == timezone.now().hour and post.schedule_time.minute == timezone.now().minute:
            post.is_published = True
            post.save()
            notification = Notification.objects.create(
                message=f'new post {post.title} by {post.author.username}',
                post=post,

            )
            notification.save()