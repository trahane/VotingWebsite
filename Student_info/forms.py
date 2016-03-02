from django import forms
from .models import studentID,Candidates
GLOBAL_VAR = []



class StudentSignUpForm(forms.ModelForm):
	class Meta:
		model = studentID
		fields = ['roll_Number','full_Name','city','state','collegeName','city','state','phone_Number']

class CandidateForm(forms.ModelForm):
	class Meta:
		model = Candidates
		fields = ['full_Name','email','phone_Number','description','collegeName']



class voteForm(forms.Form):

	def __init__(self, *args, **kwargs):

		self.user = kwargs.pop('user', None)
		super(voteForm, self).__init__(*args, **kwargs)

		uName = studentID.objects.get(userN = self.user)
		cllgName = uName.collegeName
		
		candiChoice = (Candidates.objects.all().filter(collegeName = cllgName))
		choiceInput = []
		newList=()
		i = 1
		for each in candiChoice:
			newList = (i,each)
			choiceInput.append(newList)
			i += 1
		self.fields['Select_Candidate'] = forms.ChoiceField(widget = forms.RadioSelect, choices =choiceInput)




	candiChoice = (Candidates.objects.all())
	choiceInput = []
	newList=()
	i = 1
	for each in candiChoice:
		newList = (i,each)
		choiceInput.append(newList)
		i += 1
	Select_Candidate = forms.ChoiceField(widget=forms.RadioSelect, choices=choiceInput)



