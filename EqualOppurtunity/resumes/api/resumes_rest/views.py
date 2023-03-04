from django.shortcuts import render

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

@require_http_methods(["GET"])
def list_resume_for_job(request, pk = None):
	if request.method == "GET" and pk is not None:

		job = JobAppsVO.objects.get(job_id=job)
		if job is None:
			return JsonResponse({"message": " This job application id does not exist in the database"})
	
		resumes = Resume.objects.get(job_id=pk)
			
		return JsonResponse({"Resumes": resumes}, encoder=ResumeDecoder)
	
	if request.method == "GET" and pk is None:
		return JsonResponse({"message": " Please enter a valid a valid job_id"})
	

@require_http_methods(["GET"])
def list_resume_for_job(request, pk = None):
	if request.method == "GET" and pk is None:
		return JsonResponse({"message": " Please enter a valid a valid job_id"})
		# resumes = Resume.objects.get(job_id=pk)
			
		# return JsonResponse({"Resumes": resumes}, encoder=ResumeDecoder)

# @require_http_methods(["GET"])
# def get_resumes(request, pk = None):
# 	if request.method == "GET":
# 		resumes = Resume.objects.all()
#         return JsonResponse({"Resumes": resumes}, encoder=ResumeDecoder)

        
 