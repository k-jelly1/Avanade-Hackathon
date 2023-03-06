from django.db import models

# Create your models here.
class JobPosting(models.Model):
    title = models.CharField(max_length=255)
    job_overview = models.TextField()
    requirments = models.TextField()
    good_to_have = models.TextField()
    benefits = models.TextField()
    url = models.TextField() 

    def __str__(self):
        return self.title 