"""
This is the python version of the user dataset jupyter notebook
"""


def user_psi_dataset():
    # Import libraries
    import numpy as np
    import pandas as pd

    # Read in csv file
    journal = pd.read_csv('dataset/psi_dataset.csv')
    number = len(journal)
    columns = journal.columns[21:25]

    # 4 - Calculate the mean
    mean = []
    for i in columns:
        mean_criteria = np.mean(journal[i])
        mean.append(mean_criteria)
    print("Mean: ", mean)

    # 5 - Calculate the variance
    variance = []
    for i in columns:
        variance_criteria = np.var(journal[i]) * number
        variance.append(variance_criteria)
    print("Variance: ", variance)

    # 6 - Calculate the deviation
    deviation = []
    for (i, j) in zip(columns, variance):
        deviation_criteria = 1 - j
        deviation.append(deviation_criteria)
    print("Deviation: ", deviation)

    # 7 - Calculate the Preference Value
    preference_value = []
    overall = sum(deviation)
    for (i, j) in zip(columns, deviation):
        preference_criteria = j / overall
        preference_value.append(preference_criteria)
    print("Preference Value: ", preference_value)

    sum_ = sum(preference_value)
    print(sum_)

    # 8 - Calculate the PSI
    for (i, j) in zip(columns, preference_value):
        journal[i] = journal.loc[:, i] * j

    # 9 - Creating the Ranking
    psi_rank = journal.iloc[:, 21:25]
    psi = []
    for i in range(number):
        psi_sum = sum(psi_rank.loc[i])
        psi.append(psi_sum)
    journal['psi'] = psi
    ranked_journal = journal.sort_values('psi', ascending=False)

    # 10 - Exporting to Result Ranking dataset
    ranked_journal.to_csv('dataset/result_dataset.csv', index=False)
    ranked_journal.to_csv('static/user_table.csv', index=False)
    print("Result Dataset has been created")
