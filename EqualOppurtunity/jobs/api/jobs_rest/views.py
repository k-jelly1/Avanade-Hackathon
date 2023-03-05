from django.shortcuts import render
from django.http import JsonResponse 
from .models import JobPosting
from .json import ModelEncoder
from django.views.decorators.http import require_http_methods 
# Create your views here.

#list all available job postings 

class JobAppDecoder(ModelEncoder):
    model = JobPosting
    properties = [
		"id", "title", "short_description", "description", "preferred_experience", "url"

	]


@require_http_methods(["GET"])
def get_jobs(request, pk=None):
	if request.method == "GET" and pk is None:
		jobs = JobPosting.objects.all()
		for job in jobs:
			print("Job: ", job.title)
			print("id number: ", job.id) 
		return JsonResponse({"Job Postings": jobs}, encoder=JobAppDecoder)
	else:
		job = JobPosting.objects.get(id=pk)
		if job is not None: 
			return JsonResponse({"Job ": job}, encoder=JobAppDecoder)
		return JsonResponse({"message: " "invalid job id"})
			
		
	

