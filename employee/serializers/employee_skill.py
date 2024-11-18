from rest_framework import serializers
from ..models.employee_skill import EmployeeSkill

class EmployeeSkillSerializer(serializers.ModelSerializer):
    skill_title = serializers.CharField(source = 'skill.title', read_only = True)
    
    class Meta:
        model = EmployeeSkill
        fields = "__all__"