from rest_framework import serializers
from ..models.requirement import Requirement
from ..models.project import Project
from ..models.skill import Skill

class RequirementSerializer(serializers.ModelSerializer):
    project = serializers.SlugRelatedField(read_only = False, slug_field = "title", queryset = Project.objects.all())
    skill = serializers.SlugRelatedField(read_only = False, slug_field = "title", queryset = Skill.objects.all())
    
    class Meta:
        model = Requirement
        fields = "__all__"