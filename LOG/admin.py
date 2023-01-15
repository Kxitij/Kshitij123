from django.contrib import admin
from . models import student,classes,Labs,Attendance

# Register your models here.

admin.site.register(student)
admin.site.register(classes)
admin.site.register(Labs)
admin.site.register(Attendance)