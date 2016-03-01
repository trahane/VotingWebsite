from django.contrib import admin

# Register your models here.
from .models import studentID,Candidates


class StudentIdAdmin(admin.ModelAdmin):
	list_display = ['__unicode__','userN','full_Name','email','vote','firstSignUp','city','state','phone_Number','collegeName',]

	class meta:
		model = studentID


class CandidatesAdmin(admin.ModelAdmin):
	list_display = ['__unicode__','email','description','voteCount','phone_Number','collegeName',]
	class meta:
		model = Candidates

admin.site.register(studentID,StudentIdAdmin)
admin.site.register(Candidates,CandidatesAdmin)
