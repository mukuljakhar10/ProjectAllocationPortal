from django.urls import path
from .views.project import ProjectView
from .views.skill import SkillView
from .views.notification import NotificationView

urlpatterns = [
    path('projects/', ProjectView.as_view(), name = 'project-list'),
    path('projects/<int:id>', ProjectView.get_project_by_id, name = 'project-detail'),
    path('projects/by-user', ProjectView.get_user_projects, name = 'projects-by-user'),
    path('projects/<int:id>/edit', ProjectView.as_view(), name = 'project-update'),
    path('projects/<int:id>/delete', ProjectView.as_view(), name = 'project-delete'),

    path('skills/', SkillView.as_view(), name = 'skill-list'),
    path('skills/<int:id>', SkillView.get_skill_by_id, name = 'skill-detail'),
    path('skills/<int:id>/edit', SkillView.as_view(), name = 'skill-update'),
    path('skills/<int:id>/delete', SkillView.as_view(), name = 'skill-delete'),

    path('notifications/', NotificationView.as_view(), name = 'notifications'),
    path('notifications/<int:id>', NotificationView.as_view(), name = 'upadte-notification'),
]