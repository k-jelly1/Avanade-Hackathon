from django.db import models

# Create your models here.

class JobAppsVO(models.Model):
    job_id = models.CharField(max_length=255)
    title = models.CharField(max_length=255)



class Resume(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    resume_text = models.TextField()
    # # phone = models.CharField(max_length=255)
    # work_experience = models.TextField()
    # past_projects = models.TextField()
    # certificates = models.CharField(max_length=255)
    # education = models.CharField(max_length=255)
    job = models.ForeignKey("JobAppsVO", related_name="Resume", on_delete=models.CASCADE)
    # skill= models.CharField(max_length=255)
    # reason= models.TextField()
    # value= models.TextField()
    # exp = models.PositiveSmallIntegerField(default=0)
    
    