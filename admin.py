# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Login,Students, Faculty, Admins , StudentDetails, Companyreg , CompanyName , AdminDetails , FacultyDetails , StudyMaterials,Placement

class StudentAdmin(admin.ModelAdmin):
	list_display = ('usn' , 'username' , 'dept')

admin.site.register(Placement)
admin.site.register(Login)
admin.site.register(Students)
admin.site.register(Faculty)
admin.site.register(Admins)
admin.site.register(StudentDetails)
admin.site.register(Companyreg)
admin.site.register(CompanyName)
admin.site.register(AdminDetails)
admin.site.register(FacultyDetails)
admin.site.register(StudyMaterials)
#admin.site.register(Spc)