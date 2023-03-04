import django
import os
import sys
import time
import json
import requests

sys.path.append("")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sales_project.settings")
django.setup()

# Import models from sales_rest, here.
# from sales_rest.models import Something
from sales_rest.models import AutomobileVO


def get_vins():
    response = requests.get("http://127.0.0.1:8000/api/jobs/")
    print(response)

    content = json.loads(response.content)

    for automobile in content["Job Postings"]:
        AutomobileVO.objects.update_or_create(
            vin=automobile["vin"],
            defaults={"name": automobile["model"]["name"]},
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
