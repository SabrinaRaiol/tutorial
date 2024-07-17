from django.db import models

class Task(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    completed_at = models.DateTimeField(null=True) 
    