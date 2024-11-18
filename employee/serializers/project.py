from rest_framework import serializers
from ..models.project import Project
from django.contrib.auth import get_user_model

CustomUser = get_user_model()

class ProjectSerializer(serializers.ModelSerializer):
    lead = serializers.SlugRelatedField(read_only = False, slug_field = "username", queryset = Project.objects.all())
    
    class Meta:
        model = Project
        fields = "__all__"
    
    def validate(self, data):
        
        if 'title' not in data:
            raise serializers.ValidationError('Lead field is required')
        return data