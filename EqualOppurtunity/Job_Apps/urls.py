from django.urls import path 

from .views import (get_jobs)

urlpatterns = [
	# path("locations/", get_locations, name="locations"),
	path("jobs/", get_jobs, name="jobs"),
	# path("<int:job_id>/details/", get_description, name="details"),
]