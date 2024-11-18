from django.db import models
from users.models import CustomUser

class Notification(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    message = models.TextField()
    is_seen = models.BooleanField(default=False)
    message_time = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Message for {self.user.username} : {self.message}"