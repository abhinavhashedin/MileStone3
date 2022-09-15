from rest_framework import serializers
from ProjectApp.models import Project


class ProjectAppSerializer(serializers.ModelSerializer):
 class Meta:
  model=Project
  fields = "__all__"
