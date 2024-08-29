import csv
from bert_score import score

# Define the full paths to the text files
generated_file = # This should be the file path to your generated answers as a text file
model_file = # This should be the file path to your model answers as a text file

# Load the predicted answers from "ChatGPT.txt"
with open(generated_file) as f:
    generated_answers = [line.strip() for line in f]

# Load the ground truth answers from "Model answers.txt"
with open(model_file) as f:
    model_answers = [line.strip() for line in f]

# Calculate BERT scores
P, R, F1 = score(generated_answers, model_answers, lang='en', verbose=True)

# Print the F1 score
print(f"System level F1 score: {F1.mean():.3f}")

# Iterate through individual BERT scores
for i, (p_score, r_score, f1_score) in enumerate(zip(P, R, F1)):
    print(f"Answer {i+1}:")
    print(f"Precision: {p_score:.3f}")
    print(f"Recall: {r_score:.3f}")
    print(f"F1 Score: {f1_score:.3f}")
    print()
