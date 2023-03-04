from django.contrib import admin

# Register your models here.

from .models import Resume, JobAppsVO

admin.site.register(Resume)
admin.site.register(JobAppsVO)


