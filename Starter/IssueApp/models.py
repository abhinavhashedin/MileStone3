from django.db import models
from ProjectApp.models import Project

# Create your models here.
class Issue(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.CharField(
        max_length=7,
        choices=(
            ("BUG", "BUG"),
            ("TASK", "TASK"),
            ("STORY", "STORY"),
            ("EPIC", "EPIC"),
        )
    )
    title = models.CharField(max_length=20)
    description =models.CharField(max_length=100)
    reporter=models.CharField(max_length=50)
    assignee=models.CharField(max_length=50)
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE)
    status=models.CharField(
        max_length=20,
        choices=(
            ("Open", "Open"),
            ("In Progress", "In Progress"),
            ("In Review", "In Review"),
            ("Code Complete", "Code Complete"),
            ("Done","Done")
        ),default = "Open"
    )