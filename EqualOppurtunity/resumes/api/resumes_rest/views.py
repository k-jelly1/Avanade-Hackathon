from django.shortcuts import render
import json

# Create your views here.
from django.http import JsonResponse 
from .models import Resume, JobAppsVO
from .json import ModelEncoder
from django.views.decorators.http import require_http_methods 

# Create your views here.

#list all available job postings 

class JobVODecoder(ModelEncoder):
	model = JobAppsVO
	properties = [
		"job_id", "title"
	]

class ResumeDecoder(ModelEncoder):
    model = Resume
    properties = [
		"id", "first_name", "last_name", "email", "phone", "work_experience", "past_projects", "certificates", "education", "job"
	]
    encoders = {"job": JobVODecoder()}
    

#returns all resume based on job id 
@require_http_methods(["GET", "POST"])
def list_resume_for_job(request, pk=None):
	if request.method == "GET" and pk is not None:

		# jobVO = JobAppsVO.objects.get(job_id=pk)
		# print(jobVO)
		# resumes = Resume.objects.filter(job=jobVO)
		# print(resumes)
		# print("end of try catch")
		# return JsonResponse({"resumes": resumes}, encoder=ResumeDecoder)
		try:
			jobVO = JobAppsVO.objects.get(job_id=pk)
			print(jobVO)
			resumes = Resume.objects.filter(job=jobVO)
			print(resumes)
			print("end of try catch")
			return JsonResponse({"resumes": resumes}, encoder=ResumeDecoder)
	
		except: 
			return JsonResponse({"message": "not a valid job id"})
		
	
	if request.method == "GET" and pk is None:
		return JsonResponse({"message": " Please enter a valid a valid job_id"})
	
	else: 
		#if post, request must contain resume information and job_id 
		content = json.loads(request.body)
		print(content)
		try:
			job_id = content["job_id"]
			
			JobVO = JobAppsVO.objects.get(job_id=job_id)
			
			#JobVO exists in db -> job is valid to apply for 

			# need to alter content of incoming data and format from pdf to text.
			content["job"] = JobVO
			# content["job_id"] = ""
			resume = Resume.objects.create(**content)

			return JsonResponse({"message:": "resume successfully added"})
		except JobAppsVO.DoesNotExist:
			return JsonResponse({"message:": "Please apply to a valid job posting"})
		

