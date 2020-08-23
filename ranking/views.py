from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from dataset.ranking_dataset import user_input_ranking_dataset, user_ranking_dataset
from dataset.user_dataset import user_psi_dataset
from .models import *
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
import csv
import psycopg2
import os
from psycopg2 import sql
<<<<<<< HEAD
import os
=======
>>>>>>> d1543cbd7cb0c02534aa11e944aef7b5abaeab2b
DATABASE_URL = os.environ.get('DATABASE_URL')
conn = psycopg2.connect(DATABASE_URL)
cur = conn.cursor()


@login_required
def card(request):
	if request.method == 'POST':
		card_name = request.POST.get('card_name')
		card_descr = request.POST.get('card_descr')
		card_details = Card(name=card_name, description=card_descr)
		if (Card.objects.filter(name=card_name).exists()):
			messages.info(request, 'Ranking Card Already Exist')
			return redirect('card')
		else:
			card_details.save()
			request.user.ranking_card.add(card_details)
			return redirect("rank")
	
	if request.method == 'GET':
		return render(request, "card.html")


@login_required
def rank(request):
	latest_card = Card.objects.all().last()
	latest_card = str(latest_card)
	if request.method=='GET':
		return render(request, "ranking.html", {'card_name': latest_card})
	
	if request.method=='POST':
		# index (2)
		index_first, index_second  = [], []
		# publisher (7)
		publisher_first, publisher_second, publisher_third, publisher_fourth, publisher_fifth, publisher_sixth, publisher_seventh = [], [], [], [], [], [], []
		# percentile (4)
		percentile_first, percentile_second, percentile_third, percentile_fourth = [], [], [], []
		# frequency (9)
		frequency_first, frequency_second, frequency_third, frequency_fourth, frequency_fifth, frequency_sixth, frequency_seventh, frequency_eighth, frequency_ninth  = [], [], [], [], [], [], [], [], []
		# open_access (2)
		openaccess_first, openaccess_second = [], []

		#real_values
		subject_area = request.POST.get('subject-area')
		index = request.POST['user_index_name'].split(',')
		publisher = request.POST['user_publisher_name'].split(',')
		percentile = request.POST['user_percentile_name'].split(',')
		frequency = request.POST['user_frequency_name'].split(',')
		openaccess = request.POST['user_openaccess_name'].split(',')

		if subject_area == "none":
			messages.info(request, 'No Subject Area Selected')
			return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

		if (len(index) == 2):
			index_first, index_second = int(index[0]), int(index[1])
		else:
			messages.info(request, 'Complete the Index Ranking')
			return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

		if (len(publisher) == 7):
			publisher_first, publisher_second, publisher_third, publisher_fourth, publisher_fifth, publisher_sixth, publisher_seventh = int(publisher[0]), int(publisher[1]), int(publisher[2]), int(publisher[3]), int(publisher[4]), int(publisher[5]), int(publisher[6])
		else:
			messages.info(request, 'Complete the Publisher Ranking')
			return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

		if (len(percentile) == 4):
			percentile_first, percentile_second, percentile_third, percentile_fourth = int(percentile[0]), int(percentile[1]), int(percentile[2]), int(percentile[3])
		else:
			messages.info(request, 'Complete the Percentile Ranking')
			return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

		if (len(frequency) == 9):
			frequency_first, frequency_second, frequency_third, frequency_fourth, frequency_fifth, frequency_sixth, frequency_seventh, frequency_eighth, frequency_ninth  = int(frequency[0]), int(frequency[1]), int(frequency[2]), int(frequency[3]), int(frequency[4]), int(frequency[5]), int(frequency[6]), int(frequency[7]), int(frequency[8])
		else:
			messages.info(request, 'Complete the Frequency Ranking')
			return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

		if (len(openaccess) == 2):
			openaccess_first, openaccess_second = int(openaccess[0]), int(openaccess[1])
		else:
			messages.info(request, 'Complete the Open Access Ranking')
			return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
		
		user_input_ranking_dataset(int(subject_area), index_first, index_second, publisher_first, publisher_second, publisher_third, publisher_fourth, publisher_fifth, publisher_sixth, publisher_seventh, percentile_first, percentile_second, percentile_third, percentile_fourth, frequency_first, frequency_second, frequency_third, frequency_fourth, frequency_fifth, frequency_sixth, frequency_seventh, frequency_eighth, frequency_ninth, openaccess_first, openaccess_second)
		user_ranking_dataset()
		return redirect("result")


@login_required
def result(request):
	user_psi_dataset()
	if request.method == 'GET':
		latest_card = Card.objects.all().last()
		table_name = str(latest_card)
		cur.execute(
			sql.SQL("""CREATE TABLE IF NOT EXISTS {} (scopus_source_id varchar(20), title varchar(200), citesore varchar(20), percentile varchar(20), citation_count varchar(20), scholarly_output varchar(20), percent_cited varchar(20), snip varchar(20), sjr varchar(20), rank varchar(5), rank_outof varchar(5), publisher varchar(250), publication_type varchar(100), open_access varchar(20), scopus_asjc_code varchar(5), subject_area varchar(50),  quartile varchar(20), top_10 varchar(10), scopus_link varchar(200), index varchar(10), publisher2 varchar(20), percentile2 varchar(5), frequency varchar(20), journal_website varchar(500),  review_time varchar(20), open_access2 varchar(5), print_issn varchar(10), e_issn varchar(10), user_index varchar(30), user_publisher varchar(30), user_percentile varchar(30), user_frequency varchar(30), user_open_access varchar(30), psi varchar(30))""").format(sql.Identifier(table_name))
		)
		cur.execute(sql.SQL("SELECT COUNT(*) FROM {}").format(sql.Identifier(table_name)))
		result = cur.fetchone()
		if (result[0] == 0):
			csv_file = 'dataset/result_dataset.csv'
			with open(csv_file, 'r') as f:
				reader = csv.reader(f)
				next(reader)
				for row in reader:
					cur.execute(sql.SQL("INSERT INTO {} VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)").format(sql.Identifier(table_name)),row)
			conn.commit()

		#Select Querry
		postgreSQL_select_Query = sql.SQL("SELECT * FROM {}").format(sql.Identifier(table_name))
		cur.execute(postgreSQL_select_Query)
		details = cur.fetchall()
		conn.commit()

		psi_percent = []
		for i in details:
			x = "{:0.3f}%".format(float(i[-1])*100)
			psi_percent.append(x)

		foo = zip(details, psi_percent)
		return render(request, "result.html", {'card_name': table_name, 'content': foo})


@login_required
def viewrank(request, pk): 
	if request.method == 'GET':
		table_name = pk
		postgreSQL_select_Query = sql.SQL("SELECT * FROM {}").format(sql.Identifier(table_name))
		cur.execute(postgreSQL_select_Query)
		details = cur.fetchall()
		conn.commit()

		psi_percent = []
		for i in details:
			x = "{:0.3f}%".format(float(i[-1])*100)
			psi_percent.append(x)

		foo = zip(details, psi_percent)
		return render(request, "viewrank.html", {'content': foo})


@login_required
def deletecard(request, pk): 
	if request.method == 'GET':
		try:
			instance = Card.objects.get(name=pk)
			instance.delete()
			table_name = pk
			postgreSQL_select_Query = sql.SQL("DROP TABLE IF EXISTS {}").format(sql.Identifier(table_name))
			cur.execute(postgreSQL_select_Query)
			conn.commit()
			return redirect('card')

		except Card.DoesNotExist:
			instance = None
			return redirect('card')


def journals(request):
	table_name = 'journals'
	if request.method == 'GET':
		cur.execute(
			sql.SQL("""CREATE TABLE IF NOT EXISTS {} (scopus_source_id varchar(20), title varchar(200), citesore varchar(5), percentile varchar(5), citation_count varchar(5), scholarly_output varchar(5), percent_cited varchar(5), snip varchar(10), sjr varchar(10), rank varchar(5), rank_outof varchar(5), publisher varchar(250), publication_type varchar(10), open_access varchar(5), scopus_asjc_code varchar(5), subject_area varchar(50),  quartile varchar(20), top_10 varchar(10), scopus_link varchar(200), index varchar(10), publisher2 varchar(20), percentile2 varchar(5), frequency varchar(20), journal_website varchar(300),  review_time varchar(15), open_access2 varchar(5), print_issn varchar(10), e_issn varchar(10))""").format(sql.Identifier(table_name))
		)
		cur.execute(sql.SQL("SELECT COUNT(*) FROM {}").format(sql.Identifier(table_name)))
		result = cur.fetchone()
		if (result[0] == 0):
			csv_file = 'dataset/ranking_dataset.csv'
			with open(csv_file, 'r') as f:
				reader = csv.reader(f)
				next(reader)
				for row in reader:
					cur.execute(sql.SQL("INSERT INTO {} VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)").format(sql.Identifier(table_name)),row)
			conn.commit()

		######GET
		postgreSQL_select_Query = sql.SQL("SELECT * FROM {}").format(sql.Identifier(table_name))
		cur.execute(postgreSQL_select_Query)
		details = cur.fetchall()
		conn.commit()
		return render(request, "journals.html", {'content': details})


	if request.method == 'POST':
		subject_area = request.POST.get('subject-area')

		if subject_area == "none":
			messages.info(request, 'No Subject Area Selected')
			return render(request, "journals.html")

		else:
			postgreSQL_select_Query = sql.SQL("SELECT * FROM journals WHERE subject_area='{}'".format(subject_area))
			cur.execute(postgreSQL_select_Query)
			details = cur.fetchall()
			conn.commit()
			return render(request, "journals.html", {'content': details, 'subject_area': subject_area })
