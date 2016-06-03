from django.shortcuts import render

from django.http import HttpResponseRedirect

# Create your views here.

from .forms import StudentSignUpForm,CandidateForm,voteForm
from .models import studentID,Candidates



######################################################################################################################

def home(request):
	if not(request.user.is_authenticated()):
		candiForm = CandidateForm(request.POST or None)
		if candiForm.is_valid():
			candiInstance = form.save(commit = False)
			
			candiInstance.save()
			context ={
				"candiInstance":candiInstance,
			}

		return render(request,"home.html",{})
	else:
		return HttpResponseRedirect('/profileAuth')


######################################################################################################################

def profileAuth(request):

	doneFirstSignUp = False
	if len(studentID.objects.all().filter(userN = request.user)) == 0:
		pass
	else:
		doneFirstSignUp = True


	if request.user.is_authenticated():
		

		isUser = True
		doneFirstSignUp = False
		if len(studentID.objects.all().filter(userN = request.user)) == 0:
			isUser = False
		else:
			doneFirstSignUp = True


		if isUser == False:
			form = StudentSignUpForm(request.POST or None)
			if form.is_valid():
				instance = form.save(commit = False)
				instance.firstSignUp = False
				instance.email = str(request.user.email)
				instance.userN = str(request.user)
				instance.save()

				return HttpResponseRedirect('/profileAuth')

			context = {
						#"templateTitle": title,
						"form": form,
						"isUser":isUser,
						"doneFirstSignUp":doneFirstSignUp,

				}
		else:
			votingForm = voteForm(request.POST or None,user = request.user)
			getVoteFlag = studentID.objects.get(userN = request.user)

			candidatequery = Candidates.objects.all().filter(collegeName = getVoteFlag.collegeName).filter(department = getVoteFlag.department)
			
			newListCan =[]
			newListNum = []

			if votingForm.is_valid():

				choice = votingForm.cleaned_data['Select_Candidate']

				getTupleList = voteForm.choiceInput

				for each in getTupleList:
					newListNum.append(each[0])
					newListCan.append(each[1])

				
				candiName = Candidates.objects.get(full_Name = newListCan[int(choice)-1])
				if getVoteFlag.userType == 'Teacher':
					candiName.teacherVote += 1
				elif getVoteFlag.userType == 'BE':
					candiName.seniorsVote += 1
				else:
					candiName.voteCount += 1
				candiName.save()
							
				getVoteFlag.vote = True
				getVoteFlag.save()
				
			candilen = len(candidatequery)
			candilen1 = candilen
			if candilen < 3:
				candilen1 = 6
			elif candilen <= 4:
				candilen1 = 2


			context = {

					"candidatequery":candidatequery,
					"votingForm":votingForm,
					"getVoteFlag":getVoteFlag.vote,
					"thankVote":'thank you for the vote!!!',
					"candilen":candilen,
					"candilen1":candilen1,
					"doneFirstSignUp":doneFirstSignUp,

			}
		

		return render(request,"profile.html",context)
	else:
		return HttpResponseRedirect('/')

######################################################################################################################

def editPro(request):
	if request.user.is_authenticated():
	
		dataUser = studentID.objects.get(userN = request.user)
	
		getVoteFlag = studentID.objects.get(userN = request.user)

		candidatequery = Candidates.objects.all().filter(collegeName = getVoteFlag.collegeName).filter(department = getVoteFlag.department)

		candilen = len(candidatequery)
		candilen1 = candilen
		if candilen < 3:
			candilen1 = 6
		elif candilen <= 4:
			candilen1 = 2

		context = {

			"data":dataUser,

			"candidatequery":candidatequery,
			"candilen":candilen,
			"candilen1":candilen1,
		}

		return render(request,"editPro.html",context)
	else:
		return HttpResponseRedirect('/')