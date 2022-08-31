from django.urls import path

from .views import LikeToggleAPIView, ContributorView, Notifications

urlpatterns = [
    path('<int:pk>/like/', LikeToggleAPIView.as_view(), name='like_api'),
    path('contributer/', ContributorView.as_view(), name='like_api'),
    path('notifications/', Notifications.as_view(), name='notification')
]
