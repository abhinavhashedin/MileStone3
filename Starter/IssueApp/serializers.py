from rest_framework import serializers
from IssueApp.models import Issue
from ProjectApp.models import Project


class IssueAppSerializer(serializers.ModelSerializer):

 class Meta:
  model=Issue
  fields = "__all__"

 def validate_reporter(self, value):                                     
    if self.instance and value != self.instance.reporter:            
        raise serializers.ValidationError("Reporter Will Not Be Updated",safe=False)
    return value 
