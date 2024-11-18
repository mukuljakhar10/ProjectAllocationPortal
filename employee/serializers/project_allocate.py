from rest_framework import serializers
from ..models.project import Project
from users.models import CustomUser
from ..models.project_employee import ProjectEmployee
from ..models.employee_skill import EmployeeSkill

class RecommendEmployeeSerializer(serializers.ModelSerializer):
    project_id = serializers.IntegerField()
    employee_username = serializers.CharField(max_length = 100)
    
    def validate(self, attrs):
        project = Project.objects.filter(id = attrs['project_id']).first()
        employee = CustomUser.objects.filter(username = attrs['employee_username']).first()
        
        if not project:
            raise serializers.ValidationError("Project does not exist.")
        if not employee:
            raise serializers.ValidationError("Employee does not exist.")
        
        attrs['project'] = project
        attrs['employee'] = employee
        
        return attrs

class ProjectEmployeeSerializer(serializers.ModelSerializer):
    employee_username = serializers.CharField(source = 'employee.username')
    skills = serializers.SerializerMethodField()
    
    class Meta:
        model = ProjectEmployee
        fields = ['employee_username', 'role', 'skills']
    
    def get_skills(self, obj):
        
        employee_skills = EmployeeSkill.objects.filter(employee = obj.employee)
        return [
            {'skill': skill.skill.title, 'level': skill.level}
            for skill in employee_skills.select_related('skill')
        ]