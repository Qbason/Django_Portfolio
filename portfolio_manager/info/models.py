from django.db import models

# Create your models here.

class ContentWebPage(models.Model):

    #name would be used per each page
    name = models.CharField(max_length=100)
    #language
    language=models.CharField(max_length=5)
    #content would contain all needed data
    content = models.JSONField()

    def __str__(self) -> str:
        return f"{self.name} {self.content}"
