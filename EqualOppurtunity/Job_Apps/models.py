from django.db import models

# Create your models here.
class JobPosting(models.Model):
    title = models.CharField(max_length=255)
    short_description = models.TextField()
    description = models.TextField()
    preferred_experience = models.TextField()
    url = models.TextField() 

    def __str__(self):
        return self.title 
 