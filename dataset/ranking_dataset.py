"""
This is a function of the ranking dataset used in Django project
"""
# Initialization of ranking features
import numpy as np

subject_area = []
index = dict()
publisher = dict()
percentile = dict()
open_access = dict()


def user_input_ranking_dataset(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p):
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
		my_subject_area = switcher.get(a, "You entered an invalid value")
		subject_area.append(my_subject_area)
		return subject_area

	# index_function
	def user_index():
		user_input = [b, c]
		list_index = ["Scopus", "Scopus & SCIEISI"]
		value_index = np.linspace(0.0, 1.0, 3).round(3).tolist()
		for (key, value) in zip(list_index, user_input):
			index[key] = value_index[value]
		return index

	# publisher_function
	def user_publisher():
		user_input = [d, e, f, g, h, i, j]
		list_publisher = ["Springer", "Elsevier", "IEEE", "Taylor and Francis", "Inderscience", "ACM", "Others"]
		value_publisher = np.linspace(0.0, 1.0, 8).round(3).tolist()
		for (key, value) in zip(list_publisher, user_input):
			publisher[key] = value_publisher[value]
		return publisher

	# percentile_function
	def user_percentile():
		user_input = [k, l, m, n]
		list_percentile = [400, 300, 200, 100]
		value_percentile = np.linspace(0.0, 1.0, 5).round(3).tolist()
		for (key, value) in zip(list_percentile, user_input):
			percentile[key] = value_percentile[value]
		return percentile

	# open_access_function
	def user_open_access():
		user_input = [o, p]
		list_open_access = ["Yes", "No"]
		value_open_access = np.linspace(0.0, 1.0, 3).round(3).tolist()
		for (key, value) in zip(list_open_access, user_input):
			open_access[key] = value_open_access[value]
		return open_access

	# Overall ranking_dataset return statement
	user_input_ranking_return = (user_subject_area(), user_index(), user_publisher(), user_percentile(), user_open_access())
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
	not_subject_area = journal.loc[journal.iloc[:, 7] != subject_area[0]]
	journal = journal.drop(not_subject_area.index, axis=0)

	# index_main
	journal['my_index'] = journal.iloc[:, 17]
	rank_index = journal['my_index']
	for i in rank_index:
		for key in index.keys():
			if i == key:
				rank_index.replace(i, index[key], inplace=True)

	# publisher_main
	journal['my_publisher'] = journal.iloc[:, 18]
	rank_publisher = journal['my_publisher']
	for i in rank_publisher:
		for key in publisher.keys():
			if i == key:
				rank_publisher.replace(i, publisher[key], inplace=True)

	# percentile_main
	journal['my_percentile'] = journal.iloc[:, 19]
	rank_percentile = journal['my_percentile']
	for i in rank_percentile:
		for key in percentile.keys():
			if i == key:
				rank_percentile.replace(i, percentile[key], inplace=True)

	# open_access_main
	journal['my_open_access'] = journal.iloc[:, 20]
	rank_open_access = journal['my_open_access']
	for i in rank_open_access:
		for key in open_access.keys():
			if i == key:
				rank_open_access.replace(i, open_access[key], inplace=True)

	# output
	journal.to_csv('dataset/psi_dataset.csv', index=False)
	print("User Dataset has been created")
