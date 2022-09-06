from django.contrib import admin
from .models import Post, Comment, Subscriber,News, Notification, ScheduledNotice

admin.site.site_header = 'Dashboard'


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'date_posted')
    list_display_links = ('id', 'title')
    list_filter = ('author', 'date_posted')
    search_fields = ('title', 'content', 'author')
    list_per_page = 20


admin.site.register(Post, PostAdmin)
admin.site.register(Notification)
admin.site.register(ScheduledNotice)

admin.site.register(Subscriber)
admin.site.register(News)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'post',
                    'approved_comment', 'created_date')
    list_display_links = ('id', 'author', 'post')
    list_filter = ('author', 'created_date')
    list_editable = ('approved_comment', )
    search_fields = ('author', 'post')
    list_per_page = 20


admin.site.register(Comment, CommentAdmin)
