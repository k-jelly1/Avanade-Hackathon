
import json
import requests

from .models import JobAppsVO


def get_jobs():
    print("POLLER IS WORKING")
    url = "http://127.0.0.1:8000/api/jobs/"
    response = requests.get(url)
    print(response)
    content = json.loads(response.content)
    # for conference in content["conferences"]:
    #     JobAppsVO.objects.update_or_create(
    #         import_href=conference["href"],
    #         defaults={"name": conference["name"]},
    #     )






# 
# 
# 
# import django
# import os
# import sys
# import time
# import json
# import requests

# sys.path.append("")
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "EqualOppurtunity.settings")
# django.setup()

# # Import models from sales_rest, here.
# # from sales_rest.models import Something
# from Resumes.models import JobAppsVO


# def get_jobs():
#     response = requests.get("http://127.0.0.1:8000/api/jobs/")
#     print(response)

#     content = json.loads(response.content)

#     # print("JOB POSTING: ", content["Job Postings"])
    

#     for job in content["Job Postings"]:
#         JobAppsVO.objects.update_or_create(
#             job_id=job["id number"],
#             defaults={"title": job["job"]},
#         )


# def poll():
#     while True:
#         print('Resume poller polling for data')
#         try:
#             get_jobs()
#             pass
#         except Exception as e:
#             print(e, file=sys.stderr)

#         time.sleep(60)


# if __name__ == "__main__":
#     poll()
