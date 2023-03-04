import django
import os
import sys
import time
import json
import requests

sys.path.append("")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "EqualOppurtunity.settings")
django.setup()

# Import models from sales_rest, here.
# from sales_rest.models import Something
from Resumes.models import JobAppsVO


def get_vins():
    response = requests.get("http://127.0.0.1:8000/api/jobs/")
    print(response)

    content = json.loads(response.content)

    for job in content["Job Postings"]:
        JobAppsVO.objects.update_or_create(
            job_id=job["job_id"],
            defaults={"title": job["title"]},
        )


def poll():
    while True:
        print('Resume poller polling for data')
        try:
            get_vins()
            pass
        except Exception as e:
            print(e, file=sys.stderr)
        time.sleep(60)


if __name__ == "__main__":
    poll()
