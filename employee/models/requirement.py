from django.db import models
from .skill import Skill
from .project import Project

class Requirement(models.Model):
    skill_levels = [
        ("BEGINNER", "BEGINNER"),
        ("INTERMEDIATE", "INTERMEDIATE"),
        ("ADVANCED", "ADVANCED"),
    ]
    project = models.ForeignKey(Project, related_name='req_pro', on_delete=models.CASCADE)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    level_required = models.CharField(choices=skill_levels, max_length=30)
    
    def __str__(self):
        return f"{self.project}:{self.skill} {self.level_required}"