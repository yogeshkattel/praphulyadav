from pathlib import Path
from django.urls import path

from .views import LikeToggleAPIView, ContributorView, Notifications,ProfilePic

urlpatterns = [
    path('<int:pk>/like/', LikeToggleAPIView.as_view(), name='like_api'),
    path('contributer/', ContributorView.as_view(), name='like_api'),
    path('notifications/', Notifications.as_view(), name='notification'),
    path('profile_pic/', ProfilePic.as_view(), name='profile_pic'),

]
