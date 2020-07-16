"""
This is a function of the ranking dataset used in Django project
"""

#Initialization of ranking features
subject_area = []
index = dict()
publisher = dict()
percentile = dict() 
frequency = dict()
open_access = dict()


def user_input_ranking_dataset(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u):
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
		dict_index = {1: "Scopus", 2: "Others"}
		list_index = [b, c]
		rank_index = [1.0, 0.5]
		for (x, y) in zip(list_index, rank_index):
			for key in dict_index.keys():
				if x == key:
					index[dict_index[key]] = y
		return index
	
	# publisher_function
	def user_publisher():
		dict_publisher = {1: "Springer", 2: "Elsevier", 3: "IEEE", 4: "Taylor and Francis", 5: "Inderscience", 6: "ACM",
		                  7: "Others"}
		list_publisher = [d, e, f, g, h, i, j]
		rank_publisher = [1.0, 0.85, 0.7, 0.55, 0.4, 0.25, 0.1]
		for (x, y) in zip(list_publisher, rank_publisher):
			for key in dict_publisher.keys():
				if x == key:
					publisher[dict_publisher[key]] = y
		return publisher
	
	# percentile_function
	def user_percentile():
		dict_percentile = {1: 1, 2: 2, 3: 3, 4: 4}
		list_percentile = [k, l, m, n]
		rank_percentile = [1.0, 0.7, 0.5, 0.3]
		for (x, y) in zip(list_percentile, rank_percentile):
			for key in dict_percentile.keys():
				if x == key:
					percentile[dict_percentile[key]] = y
		return percentile
	
	# frequency_function
	def user_frequency():
		dict_frequency = {1: "Monthly", 2: "Bi-monthly", 3: "Quarterly", 4: "Bi-annually", 5: "Annually"}
		list_frequency = [o, p, q, r, s]
		rank_frequency = [1.0, 0.8, 0.6, 0.4, 0.2]
		for (x, y) in zip(list_frequency, rank_frequency):
			for key in dict_frequency.keys():
				if x == key:
					frequency[dict_frequency[key]] = y
		return frequency
	
	# open_access_function
	def user_open_access():
		dict_open_access = {1: "YES", 2: "NO"}
		list_open_access = [t, u]
		rank_open_access = [1.0, 0.5]
		for (x, y) in zip(list_open_access, rank_open_access):
			for key in dict_open_access.keys():
				if x == key:
					open_access[dict_open_access[key]] = y
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
	journal = pd.read_csv(r'C:\Users\Gbubemi\Documents\#Project\journal-ranker\dataset\ranking_dataset.csv')

	# subject_area_main
	not_suject_area = journal.loc[journal.iloc[:, 15] != subject_area[0]]
	journal = journal.drop(not_suject_area.index, axis=0)
	
	# index_main
	rank_index = journal.iloc[:, 24]
	for i in rank_index:
		for key in index.keys():
			if (i == key):
				rank_index.replace(i, index[key], inplace=True)
	
	# publisher_main
	rank_publisher = journal.iloc[:, 25]
	for i in rank_publisher:
		for key in publisher.keys():
			if (i == key):
				rank_publisher.replace(i, publisher[key], inplace=True)
	
	# percentile_main
	percent = journal.iloc[:, 26]
	for per in percent:
		if (per >= 0 and per <= 25):
			percent.replace(per, 4, inplace=True)
	for per in percent:
		if (per >= 25 and per <= 49):
			percent.replace(per, 3, inplace=True)
	for per in percent:
		if (per >= 50 and per <= 74):
			percent.replace(per, 2, inplace=True)
	for per in percent:
		if (per >= 75 and per <= 99):
			percent.replace(per, 1, inplace=True)
	rank_percentile = journal.iloc[:, 26]
	for i in rank_percentile:
		for key in percentile.keys():
			if (i == key):
				rank_percentile.replace(i, percentile[key], inplace=True)
	
	# frequency_main
	rank_frequency = journal.iloc[:, 27]
	for i in rank_frequency:
		for key in frequency.keys():
			if (i == key):
				rank_frequency.replace(i, frequency[key], inplace=True)
	
	# open_access_main
	rank_open_access = journal.iloc[:, 28]
	for i in rank_open_access:
		for key in open_access.keys():
			if (i == key):
				rank_open_access.replace(i, open_access[key], inplace=True)
	
	# outputation
	journal.to_csv(r'C:\Users\Gbubemi\Documents\#Project\journal-ranker\dataset\user_dataset.csv', index=False)
	print("User Dataset has been created")
    

    
