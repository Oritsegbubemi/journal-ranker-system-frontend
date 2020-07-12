"""
This is the pythonic version of the user dataset jupyter notebook
"""

def user_psi_dataset():
    
    # Import libraries
    import numpy as np
    import pandas as pd
    
    # Read in csv file
    journal = pd.read_csv(r'C:\Users\Gbubemi\Documents\#Project\journal-ranker\dataset\user_dataset.csv')
    number = len(journal)
    columns = journal.columns[24:30]
    
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
    psi_rank = journal.iloc[:, 24:30]
    psi = []
    for i in range(number):
        psi_sum = sum(psi_rank.loc[i])
        psi.append(psi_sum)
    journal['PSI'] = psi
    ranked_journal = journal.sort_values('PSI', ascending=False)
    
    # 10 - Exporting to Result Ranking dataset
    ranked_journal.to_csv(r'C:\Users\Gbubemi\Documents\#Project\journal-ranker\dataset\result_dataset.csv', index=False)
    print("File has been created")

	# Displaying the result fams
    result_dataset = pd.read_csv(r'C:\Users\Gbubemi\Documents\#Project\journal-ranker\dataset\result_dataset.csv')

    drop_columns = [result_dataset.columns[0], result_dataset.columns[10], result_dataset.columns[12], result_dataset.columns[14], result_dataset.columns[24], result_dataset.columns[25], result_dataset.columns[26], result_dataset.columns[27], result_dataset.columns[28], result_dataset.columns[29]]
    result_dataset = result_dataset.drop(drop_columns, axis=1)

    my_output = result_dataset.to_html(r'C:\Users\Gbubemi\Documents\#Project\journal-ranker\templates\user_table.html')
    print("Ranking Table has been created")
    