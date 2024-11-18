from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from ..models.project import Project
from ..serializers.project import ProjectSerializer
from django.http import JsonResponse

class ProjectView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        serializer = ProjectSerializer(data = request.data)
        if serializer.is_valid():
            project = serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    
    @api_view(['GET'])
    def get_project_by_id(request, *args, **kwargs):
        id = kwargs['id']
        try:
            project = Project.objects.get(id = id)
            serializer = ProjectSerializer(project)
            return JsonResponse(serializer.data)
        except Project.DoesNotExist:
            return JsonResponse(status= status.HTTP_404_NOT_FOUND)
    
    @api_view(['GET'])
    def get_user_projects(request, *args, **kwargs):
        user_id = int(request.query_params.get('user_id'))
        role = request.query_params.get('role')
        username = request.query_params.get('username')
        projects = Project.obejct.all()

        if user_id == 1:
            filtered_projects = projects
        elif role == 'ADMIN':
            filtered_projects = projects.filter(lead = user_id)
        elif role == 'EMPLOYEE':
            filtered_projects = projects.filter(employees__id=[user_id])
        
        serializer = ProjectSerializer(filtered_projects, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, id, *args, **kwargs):
        try:
            project = Project.objects.get(id = id)
            serializer = ProjectSerializer(project, data = request.data)
            if serializer.is_valid():
                project = serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        except Project.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    def delete(self, request, *args, **kwargs):
        try:
            project = Project.objects.get(id = id)
            project.delete()
            return Response(status = status.HTTP_204_NO_CONTENT)
        except Project.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

