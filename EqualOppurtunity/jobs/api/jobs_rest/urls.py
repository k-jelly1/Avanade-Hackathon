from django.urls import path 

from .views import (get_jobs)

urlpatterns = [
	path("jobs/<int:pk>/", get_jobs, name="jobs"),
	path("jobs/", get_jobs, name="jobs"),
]