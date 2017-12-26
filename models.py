# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.hashers import make_password

# Create your models here.
class StudentDetails(models.Model):
	usn = models.CharField(max_length = 10, primary_key=True)
	firstname = models.CharField(max_length= 20)
	lastname = models.CharField(max_length =10, default= "")
	dept = models.CharField(max_length= 3)
	CGPA = models.FloatField(default=1.00)
	DOB = models.DateField()
	email = models.EmailField()
	graduation_year = models.IntegerField()
	Boards_12_percentage = models.FloatField()
	Boards_10_marks= models.FloatField(default = 30)
	contact_number = models.CharField(max_length= 10)

	def __str__(self):
		return self.usn

class Students(models.Model):
	
	username = models.CharField(max_length= 20)
	password = models.CharField(max_length=12)
	usn = models.CharField(max_length = 10, primary_key =True)

	def __str__(self):
		return self.username

class Faculty(models.Model):
	
	username = models.CharField(max_length= 20)
	password = models.CharField(max_length=12)
	faculty_id= models.CharField(max_length = 10, primary_key =True)

	def __str__(self):
		return self.username

class Admins(models.Model):
	
	username = models.CharField(max_length= 20)
	password = models.CharField(max_length=12)
	admin_id= models.CharField(max_length = 10, primary_key =True)

	def __str__(self):
		return self.username


class Login(models.Model):
	username = models.CharField(max_length=20, primary_key=True)
	password = models.CharField(max_length=12)
	designation = models.CharField(max_length=10 , default='Student')
	class Meta:
		verbose_name_plural = "Login"

	def __str__(self):
		return self.username

	#def save(self, *args, **kwargs):
		#self.password = make_password(self.password)
    	
class Companyreg(models.Model):
	name=models.CharField(max_length=20)
	email=models.EmailField()
	contact_number=models.CharField(max_length=10)
	usn=models.CharField(max_length=10, primary_key=True)
	company_name=models.CharField(max_length=20)
	status=models.CharField(max_length=10)
	gpa=models.CharField(max_length=5, default=6)
	class Meta:
		verbose_name_plural = "Companyreg"

	def __str__(self):
		return self.usn


class CompanyName(models.Model):
	name = models.CharField(max_length=20, primary_key=True)
	email= models.EmailField()
	date=models.DateField()
	ctc=models.CharField(max_length=3)
	contact_number = models.CharField(max_length=10)
	gpacutoff= models.CharField(max_length=5 , default=6)

	class Meta:
		verbose_name_plural = "CompanyName" #removing 's' from plural name in admin name


	def __str__(self):
		return self.name

class StudyMaterials(models.Model):
	topic=models.CharField(max_length=20)
	url=models.URLField(primary_key=True)
	dept= models.CharField(max_length=3)

	class Meta:
		verbose_name_plural = "StudyMaterials"


	def __str__(self):
		return self.topic

class FacultyDetails(models.Model):
	faculty_id= models.CharField(max_length=10 ,primary_key=True)
	name = models.CharField(max_length=20)
	dept = models.CharField(max_length=3)
	email = models.EmailField()
	contact_number = models.CharField(max_length=10)

	def __str__(self):
		return self.faculty_id

class AdminDetails(models.Model):
	admin_id= models.CharField(max_length=10 ,primary_key=True)
	name = models.CharField(max_length=20)
	email = models.EmailField()
	contact_number = models.CharField(max_length=10)

	def __str__(self):
		return self.admin_id

class Placement(models.Model):
	usn = models.CharField(primary_key=True,max_length=10)
	cname= models.CharField(max_length=20)
	ctc= models.CharField(max_length=4)
	sname=models.CharField(max_length=20, default="Prateek")

	def __str__(self):
		return self.usn
	


