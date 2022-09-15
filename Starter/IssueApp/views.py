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
import logging
import datetime
import json    

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
        logger =logging.getLogger(__name__)
        logger =logging.getLogger('django')
        issues_data=JSONParser().parse(request)
        issue= Issue.objects.get(id=issues_data['id'])
        issue_serializer=IssueAppSerializer(issue,data=issues_data)
        if issue_serializer.is_valid():
           issue_serializer.save()
           logger.info({
                         "message": "*****Updated Feild Of Issue****",
                         "updated_field": issue_serializer.data,
                         "timestamp":str(datetime.datetime.now())
                         })
           return JsonResponse("Issue Updated Successfully",safe=False)
        return JsonResponse("Issue Did Not Updated Successfully ",safe=False);    

class IssuesbyId(APIView):
    permission_classes = (IsAuthenticated, )
#Gets An Issue Details With Id As An Parameter
#Get Query Works in this Format : http://127.0.0.1:8000/issue/?id=10    
    def get(self, request):
        id = request.GET['id']
        issues_filter = Issue.objects.filter(id=id)
        issues_serializer=IssueAppSerializer(issues_filter,many=True)
        return JsonResponse(issues_serializer.data,safe=False)

    def put(self, request):
        logger =logging.getLogger(__name__)
        logger =logging.getLogger('django')
        id=request.GET.get('id', None)
        issues_filter = Issue.objects.filter(id=id).first()
        issues_data=JSONParser().parse(request)
        issue_serializer=IssueAppSerializer(issues_filter,data=issues_data)
        if issue_serializer.is_valid():
           issue_serializer.save()
           logger.info({
                         "message": "*****Updated Feild Of Issue With Id As an Parameter****",
                         "updated_field": issue_serializer.data,
                         "timestamp":str(datetime.datetime.now())
                         })
           return JsonResponse("Issue Updated Successfully",safe=False)
        return JsonResponse("Issue Did Not Updated Successfully ",safe=False); 
    

class Issuesbytitle(APIView):
    permission_classes = (IsAuthenticated, )
#Gets An Issue Details With Title As An Parameter and response will also return multiple issues if sharing same title
#Get Query Works in this Format : http://127.0.0.1:8000/issue/?title=Not    
    def get(self, request):
        title=request.GET.get('title', None)
        issues_filter = Issue.objects.filter(title=title)
        issues_serializer=IssueAppSerializer(issues_filter,many=True)
        return JsonResponse(issues_serializer.data,safe=False)  