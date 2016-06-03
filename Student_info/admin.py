from django.contrib import admin

# Register your models here.
from .models import studentID,Candidates,Colleges


######################################################################################################################
class StudentIdAdmin(admin.ModelAdmin):
	list_display = ['__unicode__','userN','full_Name','email','vote','firstSignUp','city','state','phone_Number','collegeName','department','userType']

	class meta:
		model = studentID


######################################################################################################################
class CandidatesAdmin(admin.ModelAdmin):
	list_display = ['__unicode__','email','description','voteCount','seniorsVote','teacherVote','phone_Number','collegeName','department']
	class meta:
		model = Candidates

######################################################################################################################
class CollegesAdmin(admin.ModelAdmin):
	list_display = ['__unicode__','number_of_departments','contact_number','email']
	class meta:
		model = Colleges


######################################################################################################################
admin.site.register(studentID,StudentIdAdmin)
admin.site.register(Candidates,CandidatesAdmin)
admin.site.register(Colleges,CollegesAdmin)