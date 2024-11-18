from django.db import models
from .project import Project
from users.models import CustomUser

class ProjectEmployee(models.Model):
    choices = [
        ("Assigned", "Assigned"),
        ("Recommended", "Recommended"),
    ]
    
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='projectemployees')
    employee = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='projectemployees')
    role = models.CharField(choices=choices, max_length=30)
    
    def __str__(self):
        return f"{self.employee.username}: {self.role} in {self.project.title}"