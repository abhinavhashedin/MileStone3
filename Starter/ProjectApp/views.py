from django.shortcuts import render
from rest_framework.permissions import AllowAny
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from ProjectApp.models import Project
from ProjectApp.serializers import ProjectAppSerializer
from rest_framework import status;
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

class Projects(APIView):
    permission_classes = (IsAuthenticated, )

    #Retrive All The Project Details
    def get(self, request,id=0):
        projects = Project.objects.all()
        projects_serializer=ProjectAppSerializer(projects,many=True)
        return JsonResponse(projects_serializer.data,safe=False)

    #Create a project.
    def post(self, request):
       project_data=JSONParser().parse(request)
       project_serializer=ProjectAppSerializer(data=project_data)
       if project_serializer.is_valid():
          project_serializer.save()
          return JsonResponse("Project Added Successfully",safe=False)
       return JsonResponse("Failed to Add Project",safe=False)
        
    #Update an Issue by it's id but making sure reporter is not getting updated
    def put(self, request):
        project_data=JSONParser().parse(request)
        project= Project.objects.get(id=project_data['id'])
        project_serializer=ProjectAppSerializer(project,data=project_data)
        if project_serializer.is_valid():
           project_serializer.save()
           return JsonResponse("Project Updated Successfully",safe=False)
        return JsonResponse("Failed to Update the Project")

class ProjectsDeletebyId(APIView):
    permission_classes = (IsAuthenticated, )
    #Deletes an Project With Id As An Parameter
    #Get Query Works in this Format : http://127.0.0.1:8000/project/delete/?id=10
    def delete(self, request):
        id = request.GET['id']
        project= Project.objects.get(id=id)
        project.delete()
        return JsonResponse("Project Deleted Successfully",safe=False) 

#Getting a Project By Id Param
class ProjectsbyIdParam(APIView):
    permission_classes = (IsAuthenticated, )
#Gets An Project Details With Id As An Parameter
#Get Query Works in this Format : http://127.0.0.1:8000/project/search/?id=10
    def get(self,request):
        id = request.GET['id']
        project_filter = Project.objects.filter(id=id)
        project_serializer=ProjectAppSerializer(project_filter,many=True)
        return JsonResponse(project_serializer.data,safe=False)