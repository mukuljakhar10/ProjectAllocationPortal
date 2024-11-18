from django.contrib import admin
from .models.employee_skill import EmployeeSkill
from .models.notification import Notification
from .models.project import Project
from .models.project_employee import ProjectEmployee
from .models.requirement import Requirement
from .models.skill import Skill

admin.site.register(EmployeeSkill)
admin.site.register(Notification)
admin.site.register(Project)
admin.site.register(ProjectEmployee)
admin.site.register(Requirement)
admin.site.register(Skill)
