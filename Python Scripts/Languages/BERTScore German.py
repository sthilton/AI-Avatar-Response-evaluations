import csv 
from bert_score import score 

# Load the generated and reference answers from the cleaned CSV files 
generated_file = 'path_to/HPLCGermanTrained.csv' 
reference_file = 'path_to/ModelAnswersGerman.csv' 

# Read the generated and reference answers 
with open(generated_file, 'r', encoding='utf-8') as f: 
    reader = csv.reader(f) 
    generated_answers = [row[1].strip() for row in reader]  # Assuming answers are in the second column 

with open(reference_file, 'r', encoding='utf-8') as f: 
    reader = csv.reader(f) 
    reference_answers = [row[1].strip() for row in reader]  # Assuming answers are in the second column 

# Calculate BERT scores using a model that supports German (multilingual BERT) 
P, R, F1 = score(generated_answers, reference_answers, lang='de', model_type='bert-base-multilingual-cased', verbose=True) 
  
# Print system-level F1 score 
print(f"System level F1 score: {F1.mean():.3f}") 

# Print individual precision, recall, and F1 scores for each answer 
for i, (p_score, r_score, f1_score) in enumerate(zip(P, R, F1)): 
    print(f"Answer {i+1}:") 
    print(f"Precision: {p_score:.3f}") 
    print(f"Recall: {r_score:.3f}") 
    print(f"F1 Score: {f1_score:.3f}") 
    print() 
