from django import forms
from tcp.models import Login, Students, Faculty , Admins , StudentDetails , Companyreg , FacultyDetails , AdminDetails , CompanyName , StudyMaterials,Placement


class LoginForm(forms.ModelForm):
	username = forms.CharField(max_length=128, help_text="Please enter the name.")
	password = forms.CharField(widget = forms.PasswordInput() , help_text ='Please enter your password')
	designation = forms.CharField(max_length= 10, help_text ='Please enter your designation')

	class Meta:
		model = Login
		fields = ['username' , 'password', 'designation']

class StudentForm(forms.ModelForm):
	username = forms.CharField(max_length=128, help_text="Please enter the name.")
	password = forms.CharField(widget = forms.PasswordInput(), help_text = 'please enter the password')
	usn= forms.CharField(max_length=10 , help_text = "Please enter the USN")

	class Meta:
		model = Students
		fields = ['username' , 'password' , 'usn']


class FacultyForm(forms.ModelForm):
	username = forms.CharField(max_length=10 , help_text = "Please enter the name")
	password = forms.CharField(widget = forms.PasswordInput() , help_text = 'Please enter the password')
	faculty_id = forms.CharField(max_length=10, help_text= "Please enter your id")

	class Meta:
		model = Faculty
		fields= ['username' , 'password' , 'faculty_id']


class AdminForm(forms.ModelForm):
	username = forms.CharField(max_length=128, help_text="Please enter the name.")
	password = forms.CharField(widget = forms.PasswordInput(), help_text = 'please enter the password')
	admin_id= forms.CharField(max_length=10 , help_text = "Please enter the id")
	

	class Meta:
		model = Admins
		fields = ['username' , 'password' , 'admin_id']


class StudentDetailsForm(forms.ModelForm):
	usn = forms.CharField(max_length =10, help_text="Please enter the USN.")
	firstname = forms.CharField(max_length= 20, help_text="Please enter the FirstName.")
	lastname = forms.CharField(max_length= 20, help_text="Please enter the LastName.")
	dept = forms.CharField(max_length= 3, help_text="Please enter the Department.")
	CGPA = forms.FloatField(help_text="Please enter the CGPA.")
	DOB = forms.CharField(help_text="Please enter the DOB.")
	email = forms.EmailField(help_text="Please enter the email.")
	graduation_year = forms.CharField(help_text="Please enter the Graduation_Year.")
	Boards_12_percentage = forms.CharField(help_text="Please enter the 12_Boards Percentage.")
	Boards_10_marks= forms.CharField(help_text="Please enter the Boards_10_marks.")
	contact_number = forms.CharField(max_length= 10, help_text="Please enter the Contact Number.")

	class Meta:
		model = StudentDetails
		fields = ['usn', 'firstname' , 'lastname', 'dept' , 'CGPA' , 'DOB' , 'email' , 'graduation_year', 'Boards_12_percentage' , 'Boards_10_marks' ,'contact_number']


class CompanyregForm(forms.ModelForm):
	name= forms.CharField(max_length= 20, help_text="Please enter the Name.")
	email= forms.EmailField(help_text="Please enter the email.")
	contact_number= forms.CharField(max_length= 10, help_text="Please enter the Contact Number.")
	usn= forms.CharField(max_length =10, help_text="Please enter the USN.")
	company_name=forms.CharField(max_length =10, help_text="Please enter the Company Name.")
	status=forms.CharField(max_length =10, help_text="Please enter the status(Writing or Non-Writing).")
	gpa=forms.CharField(max_length=5, help_text="PLease enter your CGPA")

	class Meta:
		model = Companyreg
		fields = ['name', 'email', 'contact_number', 'usn', 'company_name','status' , 'gpa']


class FacultyDetailsForm(forms.ModelForm):
	faculty_id= forms.CharField(max_length=10, help_text="Please enter the Faculty_ID.")
	name = forms.CharField(max_length=20, help_text="Please enter the Name.")
	dept = forms.CharField(max_length=3, help_text="Please enter the Department.")
	email = forms.EmailField(help_text="Please enter the email.")
	contact_number = forms.CharField(max_length=10, help_text="Please enter the Contact Number.")	

	class Meta:
		model= FacultyDetails
		fields = ['faculty_id', 'name', 'dept', 'email' , 'contact_number']



class AdminDetailsForm(forms.ModelForm):
	admin_id= forms.CharField(max_length=10, help_text="Please enter the Admin_ID.")
	name = forms.CharField(max_length=20, help_text="Please enter the Name.")
	email = forms.EmailField(help_text="Please enter the email.")
	contact_number = forms.CharField(max_length=10, help_text="Please enter the Contact Number.")	

	class Meta:
		model= AdminDetails
		fields = ['admin_id', 'name', 'email' , 'contact_number']


class StudyMaterialsForm(forms.ModelForm):
	topic=forms.CharField(max_length=20, help_text="Please enter the Topic Name.")
	url=forms.URLField(help_text = "Please enter the Topic URL.")
	dept=forms.CharField(max_length=3, help_text="Please enter the Department.")

	class Meta:
		model=StudyMaterials
		fields=['topic', 'url', 'dept']

class CompanyNameForm(forms.ModelForm):
	name=forms.CharField(help_text="Please enter the Name of the Company")
	email=forms.EmailField(help_text="Please enter the email id")
	date=forms.DateField(help_text="Please enter the Date of Visiting of Company.")
	ctc=forms.CharField(help_text="Please enter the CTC ")
	contact_number=forms.CharField(help_text="Please enter the Contact Number")
	gpacutoff= forms.CharField(help_text="Please enter the gpa cutoff")
	class Meta:
		model=CompanyName
		fields = ['name' , 'email', 'date' , 'ctc', 'contact_number', 'gpacutoff']

class PlacementForm(forms.ModelForm):
	usn= forms.CharField(help_text="Please enter the USN")
	cname= forms.CharField(help_text="Please enter the company name")
	ctc= forms.CharField(help_text= "Please enter the CTC")
	sname = forms.CharField(help_text= "Please enter the Student Name")
	class Meta:
		model=Placement
		fields= ['usn','cname', 'ctc', 'sname']