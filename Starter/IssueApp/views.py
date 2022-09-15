from django.shortcuts import render
from rest_framework.permissions import AllowAny
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from IssueApp.models import Issue
from IssueApp.serializers import IssueAppSerializer
from rest_framework import status;
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView



class Issues(APIView):
    permission_classes = (IsAuthenticated, )

    #Getting a list of all issues and subsequent assignee, reporter.
    def get(self, request,id=0):
        issues = Issue.objects.all()
        issues_serializer=IssueAppSerializer(issues,many=True)
        return JsonResponse(issues_serializer.data,safe=False)

     #Create an issue under a project by using project id or project name -> Project Id Passed As an Argument of Foreign Key  
    def post(self, request):
        issues_data=JSONParser().parse(request)
        issues_serializer=IssueAppSerializer(data=issues_data)
        if issues_serializer.is_valid():
            issues_serializer.save()
            return JsonResponse("Issues Added Successfully",safe=False)
        return JsonResponse(issues_serializer.errors,safe=False)
        
    #Update an Issue by it's id but making sure reporter is not getting updated
    def put(self, request):
        issues_data=JSONParser().parse(request)
        issue= Issue.objects.get(id=issues_data['id'])
        issue_serializer=IssueAppSerializer(issue,data=issues_data)
        if issue_serializer.is_valid():
           issue_serializer.save()
           return JsonResponse("Issue Updated Successfully",safe=False)
        return JsonResponse(issue_serializer.errors,status=status.HTTP_400_BAD_REQUEST);    

class IssuesbyId(APIView):
    permission_classes = (IsAuthenticated, )
#Gets An Issue Details With Id As An Parameter
#Get Query Works in this Format : http://127.0.0.1:8000/issue/?id=10    
    def get(self, request):
        id = request.GET['id']
        issues_filter = Issue.objects.filter(id=id)
        issues_serializer=IssueAppSerializer(issues_filter,many=True)
        return JsonResponse(issues_serializer.data,safe=False)

class Issuesbytitle(APIView):
    permission_classes = (IsAuthenticated, )
#Gets An Issue Details With Title As An Parameter and response will also return multiple issues if sharing same title
#Get Query Works in this Format : http://127.0.0.1:8000/issue/?title=Not    
    def get(self, request):
        title=request.GET.get('title', None)
        issues_filter = Issue.objects.filter(title=title)
        issues_serializer=IssueAppSerializer(issues_filter,many=True)
        return JsonResponse(issues_serializer.data,safe=False)