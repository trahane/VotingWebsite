from django.shortcuts import render

# Create your views here.

from .forms import StudentSignUpForm,CandidateForm,voteForm
from .models import studentID,Candidates

def home(request):
	candiForm = CandidateForm(request.POST or None)
	if candiForm.is_valid():
		candiInstance = form.save(commit = False)
		candiInstance.save()
		context ={
			"candiInstance":candiInstance,
		}

	return render(request,"home.html",{})



def profileAuth(request):
	
	isUser = True
	runUser = str(request.user)
	if len(studentID.objects.all().filter(userN = request.user)) == 0:
		isUser = False

	if isUser == False:
		form = StudentSignUpForm(request.POST or None)
		if form.is_valid():
			instance = form.save(commit = False)
			instance.firstSignUp = False
			instance.email = str(request.user.email)
			instance.userN = str(request.user)
			instance.save()		


		context = {
					#"templateTitle": title,
					"form": form,
					"isUser":isUser,

			}
	else:
		votingForm = voteForm(request.POST or None)#,userX = request.user)
		getVoteFlag = studentID.objects.get(userN = request.user)
		candidatequery = Candidates.objects.all()
		newListCan =[]
		newListNum = []
		if votingForm.is_valid():
			choice = votingForm.cleaned_data['Select_Candidate']
			print choice
			getTupleList = voteForm.choiceInput
			for each in getTupleList:
				newListNum.append(each[0])
				newListCan.append(each[1])

			
			candiName = Candidates.objects.get(full_Name = newListCan[int(choice)-1])
			candiName.voteCount += 1
		#	candiName.save()
						
			getVoteFlag.vote = True
		#	getVoteFlag.save()
			
				

		context = {

				"candidatequery":candidatequery,
				"votingForm":votingForm,
				"getVoteFlag":getVoteFlag.vote,
				"thankVote":'thank you for the vote!!!',

		}
	

	return render(request,"profile.html",context)

