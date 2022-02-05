from django.contrib import admin
from .models import Interview

# Register your models here.


class InterviewAdminInline(admin.ModelAdmin):
    module = Interview


admin.site.register(Interview, InterviewAdminInline)