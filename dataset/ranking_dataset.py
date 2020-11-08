"""
This is a function of the ranking dataset used in Django project
"""
#Initialization of ranking features
import numpy as np

subject_area = []
index = dict()
publisher = dict()
percentile = dict() 
frequency = dict()
open_access = dict()


def user_input_ranking_dataset(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y):
	"""
	This function is going to collect the user input and
	place ranking value on them as expected.
	"""

	# subject_area_function
	def user_subject_area():
		switcher = {
			1: "General Computer Science",
			2: "Computer Science (miscellaneous)",
			3: "Artificial Intelligence",
			4: "Computational Theory and Mathematics",
			5: "Computer Graphics and Computer-Aided Design",
			6: "Computer Networks and Communications",
			7: "Computer Science Applications",
			8: "Computer Vision and Pattern Recognition",
			9: "Hardware and Architecture",
			10: "Human-Computer Interaction",
			11: "Information Systems",
			12: "Signal Processing",
			13: "Software"
		}
		my_subject_area = switcher.get(a, "You entered an invalid input")
		subject_area.append(my_subject_area)
		return subject_area
	
	# index_function
	def user_index():
		# dict_index = {1: "Scopus", 2: "SCIEISI"}
		dict_index = {2: "Scopus", 1: "SCIEISI"}
		list_index = [b, c]
		rank_index = np.linspace(1, 0.1, 2).round(2).tolist()
		for (x, y) in zip(list_index, rank_index):
			for key in dict_index.keys():
				if x == key:
					index[dict_index[key]] = y
		return index
	
	# publisher_function
	def user_publisher():
		# dict_publisher = {1: "Springer", 2: "Elsevier", 3: "IEEE", 4: "Taylor and Francis", 5: "Inderscience", 6: "ACM", 7: "Others"}
		dict_publisher = {7: "Springer", 6: "Elsevier", 5: "IEEE", 4: "Taylor and Francis", 3: "Inderscience", 2: "ACM", 1: "Others"}
		list_publisher = [d, e, f, g, h, i, j]
		rank_publisher = np.linspace(1, 0.1, 7).round(2).tolist()
		for (x, y) in zip(list_publisher, rank_publisher):
			for key in dict_publisher.keys():
				if x == key:
					publisher[dict_publisher[key]] = y
		return publisher
	
	# percentile_function
	def user_percentile():
		#dict_percentile = {1: 1, 2: 2, 3: 3, 4: 4}
		dict_percentile = {1: 10, 2: 20, 3: 30, 4: 40}
		list_percentile = [k, l, m, n]
		rank_percentile = np.linspace(1, 0.1, 4).round(2).tolist()
		for (x, y) in zip(list_percentile, rank_percentile):
			for key in dict_percentile.keys():
				if x == key:
					percentile[dict_percentile[key]] = y
		return percentile
	
	# frequency_function
	def user_frequency():
		# dict_frequency = { 1: "Weekly", 2: "Fortnightly", 3: "Semi-monthly", 4: "Monthly", 5: "Bi-monthly", 6: "Quarterly", 7: "Tri-annual", 8: "Semi-annual", 9: "Annual" }
		dict_frequency = { 9: "Weekly", 8: "Fortnightly", 7: "Semi-monthly", 6: "Monthly", 5: "Bi-monthly", 4: "Quarterly", 3: "Tri-annual", 2: "Semi-annual", 1: "Annual" }
		list_frequency = [o, p, q, r, s, t, u, v, w]
		rank_frequency = np.linspace(1, 0.1, 9).round(2).tolist()
		for (x, y) in zip(list_frequency, rank_frequency):
			for key in dict_frequency.keys():
				if x == key:
					frequency[dict_frequency[key]] = y
		return frequency
	
	# open_access_function
	def user_open_access():
		# dict_open_access = {1: "Yes", 2: "No"}
		dict_open_access = {2: "Yes", 1: "No"}
		list_open_access = [x, y]
		rank_open_access = np.linspace(1, 0.1, 2).round(2).tolist()
		for (x_, y_) in zip(list_open_access, rank_open_access):
			for key in dict_open_access.keys():
				if x_ == key:
					open_access[dict_open_access[key]] = y_
		return open_access
	
	# Overall ranking_dataset return statement
	user_input_ranking_return = (user_subject_area(), user_index(), user_publisher(), user_percentile(), user_frequency(), user_open_access())
	return user_input_ranking_return



###############################################################################
def user_ranking_dataset():
	"""
	This function is going to replace the content in Ranking Dataset.csv
	with the ranking value of the user input
	"""
	
	# import libraries
	import pandas as pd
	journal = pd.read_csv('dataset/ranking_dataset.csv')

	# subject_area_main
	not_suject_area = journal.loc[journal.iloc[:, 15] != subject_area[0]]
	journal = journal.drop(not_suject_area.index, axis=0)
	
	# index_main
	journal['my_index'] = journal.iloc[:, 19]

	rank_index = journal['my_index']
	for i in rank_index:
		for key in index.keys():
			if (i == key):
				rank_index.replace(i, index[key], inplace=True)
	
	# publisher_main
	journal['my_publisher'] = journal.iloc[:, 20]

	rank_publisher = journal['my_publisher']
	for i in rank_publisher:
		for key in publisher.keys():
			if (i == key):
				rank_publisher.replace(i, publisher[key], inplace=True)
	
	# percentile_main
	journal['my_percentile'] = journal.iloc[:, 21]

	rank_percentile = journal['my_percentile']
	for i in rank_percentile:
		for key in percentile.keys():
			if (i == key):
				rank_percentile.replace(i, percentile[key], inplace=True)
	
	# frequency_main
	journal['my_frequency'] = journal.iloc[:, 22]

	rank_frequency = journal['my_frequency'] 
	for i in rank_frequency:
		for key in frequency.keys():
			if (i == key):
				rank_frequency.replace(i, frequency[key], inplace=True)
	
	# open_access_main
	journal['my_open_access'] = journal.iloc[:, 25]

	rank_open_access = journal['my_open_access']
	for i in rank_open_access:
		for key in open_access.keys():
			if (i == key):
				rank_open_access.replace(i, open_access[key], inplace=True)
	
	# outputation
	journal.to_csv('dataset/user_dataset.csv', index=False)
	print("User Dataset has been created")