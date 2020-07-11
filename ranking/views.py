from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from dataset.ranking_dataset import user_ranking_dataset, ranking_dataset
from dataset.user_dataset import user_psi_dataset
from .models import *


@login_required
def card(request):
	if request.method == 'POST':
		card_name = request.POST.get('card_name')
		card_descr = request.POST.get('card_descr')
		card_details = Card(name=card_name, description=card_descr)
		#card_exists = Card.objects.filter(name=card_name).exists()
		card_details.save()
		request.user.ranking_card.add(card_details)
		print("Card Created")
		return render(request, "ranking.html", {'card_name': card_name})
		
		#return redirect("/ranking/card")

	if request.method == 'GET':
		return render(request, "card.html")
		

@login_required
def rank(request):
	if request.method == 'POST':
		# subject_area (1)
		subject_area = request.POST.get('subject-area')
		# index (2)
		index_first = request.POST['input-index-first']
		index_second = request.POST['input-index-second']
		# publisher (7)
		publisher_first = request.POST['input-pub-first']
		publisher_second = request.POST['input-pub-second']
		publisher_third = request.POST['input-pub-third']
		publisher_fourth = request.POST['input-pub-fourth']
		publisher_fifth = request.POST['input-pub-fifth']
		publisher_sixth = request.POST['input-pub-sixth']
		publisher_seventh = request.POST['input-pub-seventh']
		# percentile (4)
		percentile_first = request.POST['input-percent-first']
		percentile_second = request.POST['input-percent-second']
		percentile_third = request.POST['input-percent-third']
		percentile_fourth = request.POST['input-percent-fourth']
		# frequency (5)
		frequency_first = request.POST['input-freq-first']
		frequency_second = request.POST['input-freq-second']
		frequency_third = request.POST['input-freq-third']
		frequency_fourth = request.POST['input-freq-fourth']
		frequency_fifth = request.POST['input-freq-fifth']
		# open_access (2)
		open_access_first = request.POST['input-access-first']
		open_access_second = request.POST['input-access-second']
		# review_time (5)
		review_time_first = request.POST['input-review-first']
		review_time_second = request.POST['input-review-second']
		review_time_third = request.POST['input-review-third']
		review_time_fourth = request.POST['input-review-fourth']
		review_time_fifth = request.POST['input-review-fifth']
		print("Save all your input")
		
		# call the ranking functions
		user_ranking_dataset(int(subject_area), int(index_first), int(index_second), int(publisher_first), int(publisher_second), int(publisher_third), int(publisher_fourth), int(publisher_fifth), int(publisher_sixth), int(publisher_seventh), int(percentile_first), int(percentile_second), int(percentile_third), int(percentile_fourth), int(frequency_first), int(frequency_second), int(frequency_third), int(frequency_fourth), int(frequency_fifth), int(open_access_first), int(open_access_second), int(review_time_first), int(review_time_second), int(review_time_third), int(review_time_fourth), int(review_time_fifth))
		ranking_dataset()
		return redirect("result")
	
	
	if request.method == 'GET':
		return render(request, "ranking.html")



def result(request):
	hello = user_psi_dataset()
	#table = r'C:\Users\Gbubemi\Documents\#Project\journal-ranking-system-frontend\journals\dataset\UserTable.html'

	
	return render(request, "result.html", {'journal': hello})
	# table = r'table.html'
	# return render(request, ("result.html", "table.html"))