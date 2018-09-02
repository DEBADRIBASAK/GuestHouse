from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from .models import Student,Company
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
# Create your views here.
def home(request):
	return render(request,'home.html',{})
def register(request):
	if request.method=='POST':
		obj = User()
		obj.username = request.POST['username']
		obj.password = request.POST['password']
		obj.save()
		student_obj = Student()
		student_obj.username = obj
		student_obj.Name = request.POST['Name']
		student_obj.Branch = request.POST['Branch']
		student_obj.CGPA = request.POST['CGPA']
		try:
			student_obj.CV = request.FILES['Resume']
		except:
			print("no file")
		student_obj.save()
		return redirect('/TnP/home')
	return render(request,'signup.html',{})

def login(request):
	response = {}
	a = request.user.is_authenticated
	if a and request.user.is_staff:
		logout(request)
		return render(request,'Log_in1.html',response)
	elif a:
		obj1 = request.user
		obj = Student.objects.get(username=obj1)
		return render(request,'Profile.html',{'student':obj})
	elif request.method=='POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username,password=password)
		if user is None:
			print('username = ',username,' ',password)
			return render(request,'Log_in1.html',{'isValid':False})
		else:
			login(request,user)
			obj = Student.objects.get(username=user)
			return render(request,'Profile.html',{student:obj})
	return render(request,'Log_in1.html',{'isValid':True})

def addCompanies(request):
	response = {}
	if request.method=='POST':
		obj = Company()
		obj.Name = request.POST['Company Name']
		obj.Description = request.POST['Description']
		obj.save()
		return redirect('/TnP/addcomp')
	return render(request,'addCompany.html',response)

def explore(request):
	obj1 = Student.objects.get(username=request.user)
	companies = Company.objects.filter(CutOff__lte=obj1.CGPA)
	return render(request,'comapnies.html',{'comapnies':companies})

def apply(request,companyID):
	obj = Company.objects.get(companyID=companyID)
	obj1 = Company.objects.get(username=request.user)
	obj.StudentsApplied.add(obj1)
	return render(request,'comapnies.html',{'comapnies':companies})





