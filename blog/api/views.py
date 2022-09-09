from cgitb import reset
from re import I
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response

from blog.models import Post, Notification
from users.models import contributors
from users.models import Profile
from rest_framework.serializers import ModelSerializer


class LikeToggleAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, pk, format=None):
        post_qs = Post.objects.get(pk=pk)
        message = "Not allowed"
        if request.user.is_authenticated:
            is_liked = Post.objects.like_toggle(request.user, post_qs)
            liked_count = post_qs.liked.all().count()
            return Response({'liked': is_liked, 'likes_count': liked_count})
        return Response({"message": message}, status=400)

# api serializer for contributors ap i


# profile view API
class ContributorView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        is_contributor = contributors.objects.filter(user=request.user).exists()
        return Response({'is_contributor': is_contributor})

class NotificationSerializer(ModelSerializer):
    class Meta:
        model = Notification
        fields = ['message', 'post']

class Notifications(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        notifications = Notification.objects.all()
        serializer = NotificationSerializer(notifications, many=True)
        return Response(serializer.data)

class ProfilePic(APIView):
    permission_classes = [permissions.IsAuthenticated]

    # get the proficle pic url for the user
    def get(self, request):
        profile = Profile.objects.filter(user=request.user).get()
        return Response({'profile_pic': profile.image.url})