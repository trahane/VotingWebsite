from django import forms
from .models import studentID,Candidates




class StudentSignUpForm(forms.ModelForm):
	class Meta:
		model = studentID
		fields = ['roll_Number','full_Name','city','state','collegeName','city','state','phone_Number']

class CandidateForm(forms.ModelForm):
	class Meta:
		model = Candidates
		fields = ['full_Name','email','phone_Number','description','collegeName']

class voteForm(forms.Form):
	# global GLOBAL_VAR 
	# GLOBAL_VAR = "ac"

	# def __init__(self, *args, **kwargs):
	# 	user = kwargs.pop('userX')
	# 	super(voteForm, self).__init__(*args, **kwargs)
	# 	if user:
	# 		#print user
	# 		userColl = studentID.objects.get(userN = user)
	# 		UNAME = userColl.collegeName
	# 		print str(UNAME)+'init'
	# 		GLOBAL_VAR = UNAME
	# 		print GLOBAL_VAR

	# print GLOBAL_VAR


	
	candiChoice = (Candidates.objects.all())
	choiceInput = []
	newList=()
	i = 1
	for each in candiChoice:
		newList = (i,each)
		choiceInput.append(newList)
		i += 1
	Select_Candidate = forms.ChoiceField(widget=forms.RadioSelect, choices=choiceInput)



