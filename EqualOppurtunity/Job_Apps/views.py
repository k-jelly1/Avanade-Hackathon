from django.shortcuts import render
from django.http import JsonResponse 
from .models import JobPosting
from .common.json import ModelEncoder
from django.views.decorators.http import require_http_methods 
# Create your views here.

#list all available job postings 

class JobAppDecoder(ModelEncoder):
    model = JobPosting
    properties = [
		"id", "title", "short_description", "description", "preferred_experience", "url"

	]


@require_http_methods(["GET"])
def get_jobs(request):
	if request.method == "GET":
		jobs = JobPosting.objects.all()
		# for job in jobs:
		# 	print("Job: ", job.title)
		# 	print("id number: ", job.id) 
			
			
		return JsonResponse({"Job Postings": jobs}, encoder=JobAppDecoder)