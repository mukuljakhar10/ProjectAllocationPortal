from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from rest_framework.response import Response
from rest_framework import status
from ..models.notification import Notification
from ..serializers.notification import NotificationSerializer
from users.models import CustomUser

class NotificationView(APIView):
    
    def get(self, request):
        user = request.user
        notifications = Notification.objects.filter(user = user, is_seen = False)
        serializer = NotificationSerializer(notifications, many = True)
        return Response(serializer.data, status = status.HTTP_200_OK)
    
    def post(self, request):
        username = request.data.get('user')
        message = request.data.get('message')
        user = CustomUser.obejcts.get(username = username)
        notification = Notification.objects.create(user = user, message = message)
        return Response({"id": notification.id, "message": notification.message}, status= status.HTTP_201_CREATED)
    
    def put(self, request, notification_id):
        notification = Notification.objects.get(id = notification_id)
        notification.is_seen = True
        notification.save()
        return Response(status = status.HTTP_204_NO_CONTENT)
    