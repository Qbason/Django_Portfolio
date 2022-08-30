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

#whoami - name

#JSON:
#first_info
#studied_about
#programming_languages
#end_info
#date_of_adding

#cv - name

#JSON:
#telephone_text
#telephone
#date_of_birth
#town
#work_experience_title
#work_experience(list of dict):
#   period
#   title
#   where
#education_title
#education(list of dict):
#   period
#   where
#   major
#   specialization
#   education_level
#skills_title
#skills:
#   programming:[list]
#   systems:[list]
#   network:[list]
#   others:[list]
#training_courses_title
#training_courses
#   date
#   name
#interests_title
#interests:[list]
#link_title
#link
#   github
#   microsoft
#   linkedin


#contact - name

#JSON:
#phone_number_info:str
#phone_number:str
#email_info:str
#email:str