"""
This is the pythonic version of the user dataset jupyter notebook
"""

def user_psi_dataset():
    
    # Import libraries
    import numpy as np
    import pandas as pd
    import pdfkit as pdf
    
    # Read in csv file
    journal = pd.read_csv('dataset/user_dataset.csv')
    number = len(journal)
    columns = journal.columns[28:33]
    
    # 4 - Calculate the mean
    mean = []
    for i in columns:
        mean_criteria = np.mean(journal[i])
        mean.append(mean_criteria)
    
    # 5 - Calculate the variance
    variance = []
    for i in columns:
        variance_criteria = np.var(journal[i])*number
        variance.append(variance_criteria)
    
    # 6 - Calculate the deviation
    deviation = []
    for (i, j) in zip(columns, variance):
        deviation_criteria = 1 - j
        deviation.append(deviation_criteria)
    
    # 7 - Calculate the Preference Value
    preference_value = []
    overall = sum(deviation)
    for (i, j) in zip(columns, deviation):
        preference_criteria = j/overall
        preference_value.append(preference_criteria)
    
    # 8 - Calaculate the PSI
    for (i,j) in zip(columns, preference_value): 
        journal[i] = journal.loc[:, i] * j
        
    # 9 - Creating the Ranking
    psi_rank = journal.iloc[:, 28:33]
    psi = []
    for i in range(number):
        psi_sum = sum(psi_rank.loc[i])
        psi.append(psi_sum)
    journal['PSI'] = psi
    ranked_journal = journal.sort_values('PSI', ascending=False)
    
    # 10 - Exporting to Result Ranking dataset
    ranked_journal.to_csv('dataset/result_dataset.csv', index=False)
    ranked_journal.to_csv('static/user_table.csv', index=False)
    print("Result Dataset has been created")