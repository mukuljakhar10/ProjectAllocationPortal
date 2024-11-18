from django.db import models
from users.models import CustomUser

class Project(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    is_active = models.BooleanField(default=False)
    lead = models.ForeignKey(CustomUser, related_name='lead_project', on_delete=models.CASCADE)
    employees = models.ManyToManyField(CustomUser, related_name='emp_pro', blank=True)
    
    def __str__(self):
        return self.title