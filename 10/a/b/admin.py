from django.contrib import admin
from .models import Patient, VitalSign, SocialHistory, ProblemList

# Register your models here.

admin.site.register(Patient)
admin.site.register(VitalSign)
admin.site.register(SocialHistory)
admin.site.register(ProblemList)

