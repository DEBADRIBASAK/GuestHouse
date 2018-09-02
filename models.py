from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
import datetime
# Create your models here.
class Student(models.Model):
	username = models.ForeignKey(User,unique=True,on_delete=False)
	Name = models.CharField(max_length=200,blank=False)
	CSE = 'CSE'
	ECE = 'ECE'
	EEE = 'EEE'
	MECH = 'Mech'
	CIV = 'Civil'
	CHEM = 'Chem'
	MME = 'MME'
	BIO = 'BioTech'
	BRANCH_CHOICES = ((CSE,'CSE'),
	(ECE,'ECE'),
	(EEE,'EEE'),
	(MECH,'Mech'),
	(CIV,'Civil'),
	(CHEM,'Chem'),
	(MME,'MME'),
	(BIO,'BioTech'))
	Branch = models.CharField(max_length=4,choices=BRANCH_CHOICES)
	isCoordinator = models.BooleanField(default=False)
	RegistrationNumber = models.CharField(max_length=6,blank=False)
	RollNo = models.CharField(max_length=6,blank=False)
	CV = models.FileField(default=None,upload_to='docs/')
	isPlaced = models.BooleanField(default=False)
	CGPA = models.FloatField(default=0.0,blank=False)#MinValueValidator(0.0),MaxValueValidator(10.0))

class Company(models.Model):
	CompanyID = models.CharField(max_length=10,blank=False,default=None)
	Name = models.CharField(max_length=200,blank=False)
	Description = models.TextField(blank=False)
	StudentsApplied = models.ManyToManyField(Student)
	CutOff = models.FloatField(default=0.0,blank=False)
	#StudentsEligible = models.ManyToManyField(Student)

