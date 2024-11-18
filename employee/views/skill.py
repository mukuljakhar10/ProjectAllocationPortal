from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from ..models.skill import Skill
from ..serializers.skill import SkillSerializer

class SkillView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        skills = Skill.objects.all()
        serializer = SkillSerializer(skills, many = True)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        serializer = SkillSerializer(data = request.data)
        if serializer.is_valid():
            skill = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    
    def get_skill_by_id(self, request, id):
        try:
            skill = Skill.objects.get(id = id)
            serializer = SkillSerializer(skill)
            return Response(serializer.data)
        except Skill.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    def put(self, request, *args, **kwargs):
        try:
            skill = Skill.objects.get(id = id)
            serializer = SkillSerializer(skill, data = request.data)
            if serializer.is_valid():
                skill = serializer.save()
                return JsonResponse(serializer.data)
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
        except Skill.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    def delete(self, request, *args, **kwargs):
        try:
            skill = Skill.objects.get(id = id)
            skill.delete()
            return Response(status= status.HTTP_204_NO_CONTENT)
        except Skill.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)