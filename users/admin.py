from django.contrib import admin
from .models import Profile, contributors
from django.contrib.auth.models import Group

# unregister the Group model 



class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user')
    list_display_links = ('id', 'user')
    list_filter = ('user', )
    list_per_page = 20


admin.site.register(Profile, ProfileAdmin)
admin.site.register(contributors)


