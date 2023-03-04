# celery.py
from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# set the default Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'resumes_project.settings')

app = Celery('resumes_project')

# set the broker URL and backend URL
app.conf.broker_url = 'redis://127.0.0.1:8000/api/jobs/'
# app.conf.result_backend = 'redis://localhost:6379/0'

# define the task routes
app.conf.task_routes = {
    'resumes_rest.tasks.poll_for_data': {'queue': 'data'},
}

# tasks.py
from celery import shared_task
import requests
from ..resumes_rest.models import JobAppsVO

@shared_task
def poll_for_data():
    response = requests.get('http://other-microservice.com/api/data')
    if response.status_code == 200:
        jobs = response.json()

        for job in jobs: 
            JobAppsVO.objects.update_or_create(
                job_id=job["id"],
                defaults={"title": job["title"]},
        )

       