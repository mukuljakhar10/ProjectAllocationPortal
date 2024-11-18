from django.db import models
from users.models import CustomUser
from .skill import Skill

class EmployeeSkill(models.Model):
    skill_levels = [
        ("BEGINNER", "BEGINNER"),
        ("INTERMEDIATE", "INTERMEDIATE"),
        ("ADVANCED", "ADVANCED"),
    ]
    employee = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    level = models.CharField(choices=skill_levels, max_length=30, default="BEGINNER")
    
    class Meta:
        unique_together = ('employee', 'skill')
    
    def __str__(self):
        return f"{self.employee}: {self.skill} {self.level}"