from django.contrib import admin

# Register your models here.

from .models import JobAppsVO, Resume

admin.site.register(Resume)
admin.site.register(JobAppsVO)


