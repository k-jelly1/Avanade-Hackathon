from django.shortcuts import render
import json
from django.utils.datastructures import MultiValueDict
import io
import re 
import PyPDF2
import numpy as np # linear algebra
# import joblib
# import pandas as pd

# model = joblib.load('C:/Users/kelly.jiang/projects/Avanade-Hackathon/EqualOppurtunity/resumes/api/resumes_rest/resume_parser_txt_file.txt')

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
	    "first_name", "last_name", "email", "resume_text"
	]
    # properties = [
	# 	"id", "first_name", "last_name", "email", "phone", "work_experience", "past_projects", "certificates", "education", "job"
	# ]
    encoders = {"job": JobVODecoder()}
    
# def extract_name(resume_text):
# 	nlp_text = nlp(resume_text)
    
#     # First name and Last name are always Proper Nouns
#     pattern = [{'POS': 'PROPN'}, {'POS': 'PROPN'}]
    
#     matcher.add('NAME', [pattern], on_match = None)
#     matches = matcher(nlp_text)
    
#     for match_id, start, end in matches:
#         span = nlp_text[start:end]
#         return span.text


# def noRre(self, s):
#         """
#         :type s: str
#         :rtype: str
#         """
#         global result 
#         result = ""
        
#         def expand(i, j):
#             global result 
            
#             while 0<= i and j < len(s) and s[i] == s[j]:
#                 if len(result) < j-i+1:
#                     result=s[i:j+1] 
#                 i-=1
#                 j+=1
                
#         for i in range(len(s)):
#             # if i&2 == 0:
#                 expand(i, i+1)
#             # else: 
#                 expand(i,i) 

#returns all resume based on job id 
@require_http_methods(["GET", "POST"])
def list_resume_for_job(request, pk=None):
	if request.method == "GET" and pk is not None:
		try:
		# if True: 
			jobVO = JobAppsVO.objects.get(job_id=pk)
			# print(jobVO)
			resumes = Resume.objects.filter(job=jobVO)
			
			
			print(resumes)
			for resume in resumes:
				list = []
				first_name = resume.first_name
				data = resume.resume_text
				last_name = resume.last_name
				replacement = "*" * len(first_name)
				# pattern = re.compile(re.escape(first_name), re.IGNORECASE)
				# string = pattern.sub(replacement, data)
				new_string1 = data.replace(first_name, replacement)	
				new_string2 = new_string1.replace(first_name.lower(), replacement)
				new_string2 = new_string2.replace(last_name, replacement)	
				new_string2 = new_string2.replace(last_name.lower(), replacement)
				new_string2 = new_string2.replace('\n',' ')
				

				print("Updated Resume ------  \n")
				print(new_string2)
				text = new_string2.replace("\u00b7", "-")
				text = text.replace("\u2013", "-")
				resume.resume_text = text

			# last_name = resumes.last_name
			# email = resumes.email

			
			# data.remove(first_name)
			# data.remove(last_name)

			# data.remove(email)
			replacement = "*" * len(first_name)
			new_string = data.replace(first_name, replacement)
			print(new_string)


		
			print(resumes)

			print("end of try catch")
			return JsonResponse({"resumes": resumes}, encoder=ResumeDecoder)
	
		except: 
			return JsonResponse({"message": "not a valid job id or no resumes exist for job yet"})
		
	
	if request.method == "GET" and pk is None:
		return JsonResponse({"message": " Please enter a valid a valid job_id"})
	
	else: 
		#if post, request must contain resume information and job_id 
		# content = json.loads(request.body)
		# print(content)

		try:
		
			pdf_file = request.FILES.get('pdfFile')
			# df = pd.read_csv(pdf_file)
			# predictions = model.predict(df)
			# return render(request, 'predictions.html', {'predictions': predictions})
			


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
		
			match = re.search(r"(\b[A-Z][a-z]+)\s(\b[A-Z][a-z]+\b)", data)
			first_name = match.group(1)
			last_name = match.group(2)

			print(data)
			# #extract email address 


			print(f"First name: {first_name}")
			print(f"Last name: {last_name}")

			match = re.search(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', data)
			email = match.group()
			print(f"Email: {email}")

			content = request.POST.copy()
			print(content["job_id"])

			job_vo = JobAppsVO.objects.get(job_id=content["job_id"])
			del content["job_id"]
			# content["job"] = job_vo
			# print("length of job value stored in content ", len(content["job"]))
			# print(content["job"])
			content["first_name"] = first_name
			content["last_name"] = last_name
			content["email"] = email	
			content["resume_text"] = data
			del content["q1"]
			del content["q2"]

			del content["q3"]

			del content["q4"]
			content["job"] = job_vo
			# content["job"]["job_id"] = content["job_id"]
			# content["job_id"] = int(content["job_id"][0])


			resume = Resume.objects.create(job=job_vo, first_name=content["first_name"], last_name=content["last_name"], email=content["email"], resume_text=data)
			# resume.job = job_vo
			resume.save() 
			# resume.job = job_vo

			# resume = Resume.objects.create(first_name=content["first_name"], last_name=content["last_name"], email=content["email"], job=content["job"], text = )
			
			

			# match = re.search(r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}', data)



			# phone_number = match.group()
			# print(f"Phone number: {phone_number}")
			# print(data)
			



		
			
		
			# index_space = data.index(' ')
			# first_name = data[1:index_space]
			
			# last_name = data.split()[1]

			# remove_arr = []
			# remove_arr.append(first_name)
			# remove_arr.append(last_name)
			# remove_arr.append(data.split()[0])
			# new_string = data 
			# for word in data.split():
			# 	for substring in remove_arr:
			# 		word = word.replace(substring,"*"*len(substring))
					
			# 	new_string+=word+" "

			# print(new_string.strip())
		
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
		

