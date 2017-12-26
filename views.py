# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from tcp.forms import LoginForm,StudentForm,AdminForm,FacultyForm , StudentDetailsForm, CompanyregForm ,CompanyNameForm , AdminDetailsForm , FacultyDetailsForm , StudyMaterialsForm,PlacementForm
from django.contrib.auth.hashers import make_password
from .models import Students, Admins, Faculty,CompanyName,Placement , StudyMaterials
from django.http import HttpResponseRedirect , HttpResponse
import itertools
from django.db.models import Count
import re
from fusioncharts import FusionCharts
from django.contrib import messages 
regexp = re.compile(r'1RV1[4-5]')
cntexp = re.compile(r'[7|8|9][0-9]')
# Create your views here.

def indexx(request):
    return render(request, 'tcp/firstlook.html')
	
def error(request):
	return render(request , 'tcp/error.html')

	
def student_signup(request):
    form = StudentForm()
    if request.method =='POST':
        form = StudentForm(request.POST)
        if form.is_valid():
			usn = form.cleaned_data['usn']
			if regexp.search(usn):
				form.save(commit = True)
				return index(request)
			else:
				return error(request)
        else:
            print form.errors

    return render(request , 'tcp/student_login.html', {'form':form})

def faculty_signup(request):
    form= FacultyForm()
    if request.method == 'POST':
        form = FacultyForm(request.POST)
        if form.is_valid():
            form.save(commit = True)
            return indexz(request)
        else:
            print form.errors
    return render(request, 'tcp/faculty_login.html' , {'form': form})


def admin_signup(request):
    form=AdminForm()
    if request.method=='POST':
        form=AdminForm(request.POST)
        if form.is_valid():
            form.save(commit =True)
            return indexzz(request)
        else:
            print form.errors
    return render(request , 'tcp/admin.html' , {'form' :form})

def login(request):
    form= LoginForm()
    if request.method=='POST':
        form= LoginForm(request.POST)
        if form.is_valid():
            p=form.cleaned_data['designation']
            if p=='Student':
                ch1=form.cleaned_data['username']
                ch2=form.cleaned_data['password']
                if(Students.objects.get(password=ch2)):
                    return index(request)
            elif p=='Faculty':
                ch1=form.cleaned_data['username']
                ch2=form.cleaned_data['password']
                if(Faculty.objects.get(password=ch2)):
                    return indexz(request)
            elif p=='Admin':
                ch1=form.cleaned_data['username']
                ch2=form.cleaned_data['password']
                if(Admins.objects.get(password=ch2)):
                    return indexzz(request)
            else:
                print form.errors
        else:
            print form.errors
    return render(request, 'tcp/login.html' , {'form': form})

def firstlook(request):
	return render(request, 'tcp/firstlook.html')



def index(request):
    return render(request, 'tcp/student/web/index.html')


def indexzz(request):
    return render(request, 'tcp/admin/web/index.html')


def indexz(request):
    return render(request, 'tcp/faculty/web/index.html')

def iz(request):
    return render(request, 'tcp/student/web/reg/web/ix.html')

def index_details(request):
    form = StudentDetailsForm()
    if request.method == 'POST':
        form = StudentDetailsForm(request.POST)
        if form.is_valid():
            form.save(commit = True)
            return index(request)
        else:
            print form.errors 
    return render(request, 'tcp/student/web/details/index.html' ,{'form': form})


def admin_reg(request):
    form = AdminDetailsForm()
    if request.method == 'POST':
        form = AdminDetailsForm(request.POST)
        if form.is_valid():
            form.save(commit = True)
            return indexzz(request)
        else:
            print form.errors
    return render(request, 'tcp/admin/web/details/index.html', {'form': form})


def faculty_reg(request):
    form = FacultyDetailsForm()
    if request.method == 'POST':
        form = FacultyDetailsForm(request.POST)
        if form.is_valid():
            form.save(commit = True)
            return indexz(request)
        else:
            print form.errors
    return render(request, 'tcp/faculty/web/details/index.html', {'form': form})



def test_registration(request):
    form=CompanyregForm()
    if request.method == 'POST':
        form=CompanyregForm(request.POST)
        if form.is_valid():
            p=form.cleaned_data['name']
            countt = Placement.objects.filter(sname=p)
            if countt:
                coun = Placement.objects.get(sname=p)
                if coun.ctc>8:
                    return iz(request)
                else:
                    form.save(commit = True)
                    return index(request)
            else:
				p=form.cleaned_data['gpa']
				q=form.cleaned_data['company_name']
				countt= CompanyName.objects.get(name = q)
				if countt.gpacutoff < p:
					form.save(commit=True)
					return index(request)
				else:
					return iz(request)
        else:
            print form.errors
    return render(request, 'tcp/student/web/reg/web/index.html' , {'form': form})



def update_materials(request):
    form = StudyMaterialsForm()
    if request.method == 'POST':
        form = StudyMaterialsForm(request.POST)
        if form.is_valid():
            form.save(commit= True)
            return indexz(request)
        else:
            print form.errors
    return render(request, 'tcp/faculty/web/reg/web/index.html', {'form': form})



def company_details(request):
    form= CompanyNameForm()
    if request.method=='POST':
        form=CompanyNameForm(request.POST)
        if form.is_valid():
			contact = form.cleaned_data['contact_number']
			if cntexp.search(contact):
				form.save(commit= True)
				return indexzz(request)
			else:
				print form.errors
        else:
            print form.errors
    return render(request, 'tcp/admin/web/reg/web/index.html', {'form': form})

def test(request):
    company= CompanyName.objects.raw('Select * from tcp_companyname')
    return render(request , 'tcp/test.html', {'company': company})


def statistics(request):
	le=[]
	ct = Placement.objects.raw('Select * From tcp_Placement')
	for c in ct:
		if c.cname not in le:
			le.append(c.cname)
	cnt=len(le)
	placement= Placement.objects.all().values('cname').annotate(total=Count('sname')).order_by('cname')
	countt = Placement.objects.values('ctc' , 'cname').annotate(total=Count('cname')).order_by('cname')
	place = {'placement': placement , 'countt': countt , 'cnt': cnt}
	return render(request , 'tcp/statistics.html', place)
	



def placement_reg(request):
    form=PlacementForm()
    if request.method=='POST':
        form=PlacementForm(request.POST)
        if form.is_valid():
            form.save(commit = True)
            return indexz(request)
        else:
            print form.errors
    return render(request , 'tcp/faculty/web/placement.html' , {'form': form})



def study_materials(request):
    topicname = StudyMaterials.objects.raw('Select * from tcp_StudyMaterials')
    return render(request , 'tcp/student/web/reg/web/indexes.html' , {'topicname': topicname})
	
def getdetails(request):
	form=GetdetailsForm()
	if request.method=='POST':
		form=GetdetailsForm(request.POST)
		if form .is_valid():
			id=form.cleaned_data['id']
			if regexp.search(id):
				query= StudentDetails.objects.get(id='id')
				return render(request , 'tcp/faculty/web/getid.html' , {'query' : query})
