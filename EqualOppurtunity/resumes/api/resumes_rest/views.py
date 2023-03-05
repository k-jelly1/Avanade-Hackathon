from django.shortcuts import render
import json
from django.utils.datastructures import MultiValueDict
import PyPDF2
import io
import re 

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
	    "file",
	]
    # properties = [
	# 	"id", "first_name", "last_name", "email", "phone", "work_experience", "past_projects", "certificates", "education", "job"
	# ]
    encoders = {"job": JobVODecoder()}
    

#returns all resume based on job id 
@require_http_methods(["GET", "POST"])
def list_resume_for_job(request, pk=None):
	if request.method == "GET" and pk is not None:
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
		# content = json.loads(request.body)
		# print(content)
	
		try:
			pdf_file = request.FILES.get('pdfFile')
			# print(pdf_file['Resume'])


			# pdf_file = request.FILES.get('pdfFile')
			
			pdf_data = pdf_file.read()
			# print(pdf_data)
			pdf_reader = PyPDF2.PdfReader(io.BytesIO(pdf_data))
			num_pages = len(pdf_reader.pages) 
			pdf_text=''
			for page_num in range(num_pages):
				pdf_page = pdf_reader.pages[page_num] 
				pdf_text+=pdf_page.extract_text()
			json_data = json.dumps(pdf_text)
			
			bytes_data = json_data.encode("utf-8")

			data = re.sub(r'[^\x20-\x7E]+', '', bytes_data.decode('utf-8'))
			
		
			index_space = data.index(' ')
			first_name = data[1:index_space]
			
			last_name = data.split()[1]

			remove_arr = []
			remove_arr.append(first_name)
			remove_arr.append(last_name)
			remove_arr.append(data.split()[0])
			new_string = data 
			for word in data.split():
				for substring in remove_arr:
					word = word.replace(substring,"*"*len(substring))
					
				new_string+=word+" "

			print(new_string.strip())
		
			# data = data.replace(first_name, "*" * len(first_name))
			# data = data.replace(last_name, "*" * len(last_name))	
			# data = data.replace(data.split()[0],"*" * len(data.split()[0]))	
			# print(data)

			
			# print(last_name)

			
			

			# page_text = pdf_reader.pages[1].extract_text() 

			# json_data = json.dumps({'pdf_text':page_text})
			# print(json_data)
			# num_pages = pdf_reader.getNumPages()

			# post_data = MultiValueDict(request.POST)
			# data_dict = dict(post_data.lists())
			# data_json = json.dumps(data_dict)

			# print(data_json)

			# job_id = content["job_id"]
			# print(request)
			# print(('pdf_file' in request.FILES))

			# print(resume_pdf)
			
			# JobVO = JobAppsVO.objects.get(job_id=job_id)
			
			#JobVO exists in db -> job is valid to apply for 

			# need to alter content of incoming data and format from pdf to text.
			# content["job"] = JobVO
			# content["job_id"] = ""
			# resume = Resume.objects.create(**content)

			return JsonResponse({"message:": "resume successfully added"})
		except JobAppsVO.DoesNotExist:
			return JsonResponse({"message:": "Please apply to a valid job posting"})
		

