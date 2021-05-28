from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from dataset.ranking_dataset import user_input_ranking_dataset, user_ranking_dataset
from dataset.psi_dataset import user_psi_dataset
from django.http import HttpResponseRedirect
import csv
import psycopg2
import os
from psycopg2 import sql
from django.conf import settings
from ranking.models import RankingCard

User = settings.AUTH_USER_MODEL
DATABASE_URL = os.environ['DATABASE_URL']
conn = psycopg2.connect(DATABASE_URL)
cur = conn.cursor()


@login_required
def card(request):
    if request.method == 'POST':
        card_name = request.POST.get('card_name')
        card_descr = request.POST.get('card_descr')
        new_card_name = card_name + "_" + request.user.username
        card_details = RankingCard(name=card_name, description=card_descr)
        if RankingCard.objects.filter(name=new_card_name).exists():
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
    latest_card = RankingCard.objects.all().last()
    latest_card = str(latest_card)
    if request.method == 'GET':
        return render(request, "ranking.html", {'card_name': latest_card})
    if request.method == 'POST':
        # subject area
        subject_area = request.POST.get('subject-area')
        # index
        index = []
        index_first = request.POST.get('index-first')
        index_second = request.POST.get('index-second')
        index.extend((index_first, index_second))
        # publisher
        publisher = []
        publisher_first = request.POST.get('publisher-first')
        publisher_second = request.POST.get('publisher-second')
        publisher_third = request.POST.get('publisher-third')
        publisher_fourth = request.POST.get('publisher-fourth')
        publisher_fifth = request.POST.get('publisher-fifth')
        publisher_sixth = request.POST.get('publisher-sixth')
        publisher_seventh = request.POST.get('publisher-seventh')
        publisher.extend((publisher_first, publisher_second, publisher_third, publisher_fourth,
                          publisher_fifth, publisher_sixth, publisher_seventh))
        # percentile
        percentile = []
        percentile_first = request.POST.get('percentile-first')
        percentile_second = request.POST.get('percentile-second')
        percentile_third = request.POST.get('percentile-third')
        percentile_fourth = request.POST.get('percentile-fourth')
        percentile.extend((percentile_first, percentile_second, percentile_third, percentile_fourth))
        # open access
        open_access = []
        open_access_first = request.POST.get('open-access-first')
        open_access_second = request.POST.get('open-access-second')
        open_access.extend((open_access_first, open_access_second))
        if len(list(index)) != len(set(index)):
            messages.info(request, 'The index rankings cannot have equal values')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        elif len(list(publisher)) != len(set(publisher)):
            messages.info(request, 'The publisher rankings cannot have equal values')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        elif len(list(percentile)) != len(set(percentile)):
            messages.info(request, 'The percentile rankings cannot have equal values')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        elif len(list(open_access)) != len(set(open_access)):
            messages.info(request, 'The open access rankings cannot have equal values')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            user_input_ranking_dataset(int(subject_area), int(index_first), int(index_second),
                                       int(publisher_first), int(publisher_second), int(publisher_third),
                                       int(publisher_fourth), int(publisher_fifth), int(publisher_sixth),
                                       int(publisher_seventh), int(percentile_first), int(percentile_second),
                                       int(percentile_third), int(percentile_fourth), int(open_access_first),
                                       int(open_access_second))
            user_ranking_dataset()
            return redirect("result")


@login_required
def result(request):
    user_psi_dataset()
    latest_card = RankingCard.objects.all().last()
    table_name = str(latest_card)
    cur.execute(
        sql.SQL(
            """CREATE TABLE IF NOT EXISTS {} (title varchar(200), citation_count varchar(20), 
            scholarly_output varchar(20), percent_cited varchar(20), citesore varchar(20), snip varchar(20), 
            sjr varchar(20), subject_area varchar(50), percentile varchar(20), rank varchar(20), 
            rank_out_of varchar(20), publisher varchar(250), open_access varchar(20), quartile varchar(20), 
            scopus_url varchar(200), print_issn varchar(20), e_issn varchar(20), index varchar(20), 
            publisher2 varchar(20), percentile2 varchar(20), open_access2 varchar(20), user_index varchar(30), 
            user_publisher varchar(30), user_percentile varchar(30), user_open_access varchar(30), psi varchar(30))"""
        ).format(sql.Identifier(table_name)))
    cur.execute(sql.SQL("SELECT COUNT(*) FROM {}").format(sql.Identifier(table_name)))
    _result = cur.fetchone()
    if _result[0] == 0:
        csv_file = 'dataset/result_dataset.csv'
        with open(csv_file, 'r') as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                cur.execute(sql.SQL(
                    "INSERT INTO {} VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, "
                    " %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s )"
                ).format(sql.Identifier(table_name)), row)
        conn.commit()
    # Select Querry
    postgre_sql_select_query = sql.SQL("SELECT * FROM {}").format(sql.Identifier(table_name))
    cur.execute(postgre_sql_select_query)
    details = cur.fetchall()
    conn.commit()
    psi_percent = []
    for i in details:
        x = "{:0.3f}%".format(float(i[-1]) * 100)
        psi_percent.append(x)
    show_details = details[:10]
    foo = zip(show_details, psi_percent)
    if request.method == 'GET':
        return render(request, "result.html", {'card_name': table_name, 'content': foo})
    if request.method == 'POST':
        view_number = request.POST.get('view-number')
        if view_number == "10":
            show_details = details[:10]
            foo = zip(show_details, psi_percent)
            return render(request, "result.html", {'card_name': table_name, 'content': foo})
        if view_number == "20":
            show_details = details[:20]
            foo = zip(show_details, psi_percent)
            return render(request, "result.html", {'card_name': table_name, 'content': foo})
        else:
            foo = zip(details, psi_percent)
            return render(request, "result.html", {'card_name': table_name, 'content': foo})


@login_required
def viewrank(request, pk):
    if request.method == 'GET':
        try:
            table_name = pk
            postgre_sql_select_query = sql.SQL("SELECT * FROM {}").format(sql.Identifier(table_name))
            cur.execute(postgre_sql_select_query)
            details = cur.fetchall()
            conn.commit()
            psi_percent = []
            for i in details:
                x = "{:0.3f}%".format(float(i[-1]) * 100)
                psi_percent.append(x)
            details = details[:10]
            foo = zip(details, psi_percent)
            return render(request, "viewrank.html", {'content': foo})
        except:
            return render(request, "card.html")


@login_required
def deletecard(request, pk):
    if request.method == 'GET':
        try:
            instance = RankingCard.objects.get(name=pk)
            instance.delete()
            table_name = pk
            postgre_sql_select_query = sql.SQL("DROP TABLE IF EXISTS {}").format(sql.Identifier(table_name))
            cur.execute(postgre_sql_select_query)
            conn.commit()
            return redirect('card')
        except RankingCard.DoesNotExist:
            return redirect('card')


def journals(request):
    table_name = 'journals'
    if request.method == 'GET':
        cur.execute(
            sql.SQL(
                """CREATE TABLE IF NOT EXISTS {} (title varchar(200), citation_count varchar(20), 
                scholarly_output varchar(20), percent_cited varchar(20), citesore varchar(20), snip varchar(20), 
                sjr varchar(20), subject_area varchar(50), percentile varchar(20), rank varchar(20), 
                rank_out_of varchar(20), publisher varchar(250), open_access varchar(20), quartile varchar(20), 
                scopus_url varchar(200), print_issn varchar(20), e_issn varchar(20), index varchar(20), 
                publisher2 varchar(20), percentile2 varchar(20), open_access2 varchar(20))"""
                ).format(sql.Identifier(table_name))
        )
        cur.execute(sql.SQL("SELECT COUNT(*) FROM {}").format(sql.Identifier(table_name)))
        _result = cur.fetchone()
        if _result[0] != 2524:
            csv_file = 'dataset/ranking_dataset.csv'
            with open(csv_file, 'r') as f:
                reader = csv.reader(f)
                next(reader)
                for row in reader:
                    cur.execute(sql.SQL(
                        "INSERT INTO {} VALUES (%s, %s, %s, %s, %s, %s, %s, %s, "
                        "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                    ).format(sql.Identifier(table_name)), row)
            conn.commit()

        # GET
        postgre_sql_select_query = sql.SQL("SELECT * FROM {}").format(sql.Identifier(table_name))
        cur.execute(postgre_sql_select_query)
        details = cur.fetchall()
        conn.commit()
        return render(request, "journals.html", {'content': details})

    if request.method == 'POST':
        search_title = request.POST['search-box']
        postgre_sql_select_query = sql.SQL("SELECT * FROM journals WHERE title LIKE '%{}%'".format(search_title))
        cur.execute(postgre_sql_select_query)
        details = cur.fetchall()
        conn.commit()

        if len(details) == 0:
            messages.info(request, 'No Search Result Found')
            return render(request, "journals.html", {'search_title': search_title})

        return render(request, "journals.html", {'content': details, 'search_title': search_title})
