"""
This is the pythonic version of the user dataset jupyter notebook
"""

def user_psi_dataset():
    
    # Import libraries
    import numpy as np
    import pandas as pd
    
    # Read in csv file
    journal = pd.read_csv(r'C:\Users\Gbubemi\Documents\#Project\journal-ranking-system-frontend\journals\dataset\User_Dataset.csv')
    number = len(journal)
    columns = journal.columns[2:]
    
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
    psi_rank = journal.iloc[:, 2:]
    psi = []
    for i in range(number):
        psi_sum = sum(psi_rank.loc[i])
        psi.append(psi_sum)
    journal['PSI'] = psi
    ranked_journal = journal.sort_values('PSI', ascending=False)
    
    # 10 - Exporting to Result Ranking dataset
    ranked_journal.to_csv(r'C:\Users\Gbubemi\Documents\#Project\journal-ranking-system-frontend\journals\dataset\Result_Dataset.csv', index=False)
    print("File has been created")

	# Displaying the result fams
    result_dataset = pd.read_csv(r'C:\Users\Gbubemi\Documents\#Project\journal-ranking-system-frontend\journals\dataset\Result_Dataset.csv')
    result_dataset = result_dataset.head(11)
    print("HHHHHHHHHHHHHHH", result_dataset)
    result_dataset.to_html(r'C:\Users\Gbubemi\Documents\#Project\journal-ranking-system-frontend\journals\dataset\UserTable.html')
    my_output = result_dataset.to_html()
    print("MMMMMMMMMMMMMMM", my_output)


    


    print("End of the code")
    
    return (my_output)