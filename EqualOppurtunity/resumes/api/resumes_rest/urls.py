

from django.urls import path 

from .views import (list_resume_for_job)

urlpatterns = [
	path("resumes/", list_resume_for_job, name="resumes"),
	path("resumes/<int:pk>/", list_resume_for_job, name="list_by_job"),

]
