import pandas as pd 
from sklearn.metrics import f1_score 

# Specify the full path to the CSV files 
reference_csv_path = r'path_to/ModelAnswersGerman.csv' 
generated_csv_path =  r'path_to/HPLCGermanTrained.csv'   

# Read the CSV files into dataframes 
reference_df = pd.read_csv(reference_csv_path) 
generated_df = pd.read_csv(generated_csv_path) 

# Initialize empty lists for precision, recall, and F1 scores 
precision = [] 
recall = [] 
f1_scores = [] 

# Calculate precision, recall, and F1 score for each pair of answers 
for index, row in reference_df.iterrows(): 
    reference = row['reference_answers'] 
    generated = generated_df.at[index, 'generated_answers'] 
    reference_set = set(reference.split()) 
    generated_set = set(generated.split()) 
    intersection = len(reference_set.intersection(generated_set)) 
    if len(generated_set) == 0: 
        precision.append(0) 
    else: 
        precision.append(intersection / len(generated_set)) 
    recall.append(intersection / len(reference_set)) 
    f1_scores.append( 
        2 * (precision[-1] * recall[-1]) / (precision[-1] + recall[-1]) if precision[-1] + recall[-1] > 0 else 0) 

# Calculate the average F1 score 
average_f1_score = sum(f1_scores) / len(f1_scores) 

# Print precision, recall, F1 score for each answer, and average F1 score 
for i in range(len(reference_df)): 
    print(f"Answer {i + 1}:") 
    print(f"  Precision: {precision[i]:.2f}") 
    print(f"  Recall: {recall[i]:.2f}") 
    print(f"  F1 Score: {f1_scores[i]:.2f}") 
    print() 
  
print(f"Average F1 Score: {average_f1_score:.2f}") 
