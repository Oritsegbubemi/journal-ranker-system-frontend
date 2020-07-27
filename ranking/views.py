from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from dataset.ranking_dataset import user_input_ranking_dataset, user_ranking_dataset
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
		return render(request, "ranking.html", {'card_name': card_name})

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
		# frequency (9)
		frequency_first = request.POST['input-freq-first']
		frequency_second = request.POST['input-freq-second']
		frequency_third = request.POST['input-freq-third']
		frequency_fourth = request.POST['input-freq-fourth']
		frequency_fifth = request.POST['input-freq-fifth']
		frequency_sixth = request.POST['input-freq-sixth']
		frequency_seventh = request.POST['input-freq-seventh']
		frequency_eighth = request.POST['input-freq-eighth']
		frequency_ninth = request.POST['input-freq-ninth']
		# open_access (2)
		open_access_first = request.POST['input-access-first']
		open_access_second = request.POST['input-access-second']
		print("Save all your input")

		# call the ranking functions
		user_input_ranking_dataset(int(subject_area), int(index_first), int(index_second), int(publisher_first), int(publisher_second), int(publisher_third), int(publisher_fourth), int(publisher_fifth), int(publisher_sixth), int(publisher_seventh), int(percentile_first), int(percentile_second), int(percentile_third), int(percentile_fourth), int(frequency_first), int(frequency_second), int(frequency_third), int(frequency_fourth), int(frequency_fifth), int(frequency_sixth), int(frequency_seventh), int(frequency_eighth), int(frequency_ninth), int(open_access_first), int(open_access_second))
		user_ranking_dataset()
		return redirect("result")
	
	if request.method == 'GET':
		return render(request, "ranking.html")
		

@login_required
def result(request): 
	user_psi_dataset()
	if request.method == 'GET':
		import csv
		import psycopg2
		conn = psycopg2.connect("host=localhost dbname=journals user=postgres password=gbubemi")
		cur = conn.cursor()
		cur.execute(
			"""CREATE TABLE IF NOT EXISTS user_journal (title varchar(200), citesore varchar(20), percentile varchar(20), citation_count varchar(20), scholarly_output varchar(20), percent_cited varchar(20), snip varchar(20), sjr varchar(20), publisher varchar(250), open_access varchar(20), quartile varchar(20), scopus_link varchar(200), frequency varchar(20), review_time varchar(20), print_issn varchar(20), psi varchar(20))"""
		)
		csv_file = r'C:\Users\Gbubemi\Documents\#Project\journal-ranker\dataset\short_dataset.csv'
		with open(csv_file, 'r') as f:
			reader = csv.reader(f)
			next(reader) # Skip the header row.
			for row in reader:
				cur.execute("INSERT INTO user_journal VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", row)
		conn.commit()

		import psycopg2
		conn = psycopg2.connect("host=localhost dbname=journals user=postgres password=gbubemi")
		cur = conn.cursor()
		postgreSQL_select_Query = "select * from user_journal"
		cur.execute(postgreSQL_select_Query)
		details = cur.fetchall()
		conn.commit()
		return render(request, "result.html", {'content': details})


@login_required
def viewrank(request): 
	if request.method == 'GET':
		import psycopg2
		conn = psycopg2.connect("host=localhost dbname=journals user=postgres password=gbubemi")
		cur = conn.cursor()
		postgreSQL_select_Query = "select * from user_journal"
		cur.execute(postgreSQL_select_Query)
		details = cur.fetchall()
		conn.commit()
		return render(request, "viewrank.html", {'success':'Table created', 'content': details})


#ranking2
@login_required
def ranking2(request):
	if request.method=='GET':
		return render(request, "ranking2.html")

	if request.method=='POST':
		hello = request.POST.get('collect')
		print(hello)
		return render(request, 'ranking2.html')