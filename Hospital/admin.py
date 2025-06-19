from django.contrib import admin
from .models import *

admin.site.register(Credentials)
admin.site.register(Doctor)
admin.site.register(Appointments)
admin.site.register(PatientRecords)