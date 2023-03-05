from django.shortcuts import render
import json

# Create your views here.
from django.http import JsonResponse 
from .models import Resume, JobAppsVO
from common.json import ModelEncoder
from django.views.decorators.http import require_http_methods 
# Create your views here.

#list all available job postings 

class ResumeDecoder(ModelEncoder):
    model = Resume
    properties = [
		"id", "first_name", "last_name", "email", "phone", "work_experience", "past_projects", "certificates", "education", "job_id"
	]
#returns all resume based on job id 
@require_http_methods(["GET", "POST"])
def list_resume_for_job(request, pk = None):
	if request.method == "GET" and pk is not None:

		job = JobAppsVO.objects.get(job_id=job)
		if job is None:
			return JsonResponse({"message": " This job application id does not exist in the database"})
	
		resumes = Resume.objects.get(job_id=pk)
			
		return JsonResponse({"Resumes": resumes}, encoder=ResumeDecoder)
	
	if request.method == "GET" and pk is None:
		return JsonResponse({"message": " Please enter a valid a valid job_id"})
	
	else: 
		#if post, request must contain resume information and job_id 
		content = json.loads(request.body)
		try:
			job_id = content["job_id"]
			JobVO = JobAppsVO.objects.get(job_id=job_id)
			#JobVO exists in db -> job is valid to apply for 

			# need to alter content of incoming data and format from pdf to text.
			resume = Resume.objects.create(**content)

			return JsonResponse({"message:": "resume successfully added"})
		except JobVO.DoesNotExist:
			return JsonResponse({"message:": "Please apply to a valid job posting"})
		

# @require_http_methods(["GET", "POST"])
# def list_resume_for_job(request, pk = None):
# 	if request.method == "GET" and pk is None:
# 		return JsonResponse({"message": " Please enter a valid a valid job_id"})
		# resumes = Resume.objects.get(job_id=pk)
			
		# return JsonResponse({"Resumes": resumes}, encoder=ResumeDecoder)

# @require_http_methods(["POST"])
# def get_resumes(request):
# 	if request.method == "GET":
# 		resumes = Resume.objects.all()
#         return JsonResponse({"Resumes": resumes}, encoder=ResumeDecoder)

        
 