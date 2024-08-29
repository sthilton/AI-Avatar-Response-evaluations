from nltk.translate.bleu_score import sentence_bleu, SmoothingFunction

# Read the contents of the files
with open('Model answers.txt', 'r') as ref_file:       #replace 'Model answers.txt' with the name of your text document. 
    reference_sentences = ref_file.readlines()

with open('Trained answers.txt', 'r') as cand_file:      #replace 'Trained answers.txt' with the name of your text document. 
    candidate_sentences = cand_file.readlines()

# Ensure you have the same number of sentences in both files
assert len(reference_sentences) == len(candidate_sentences), "The number of sentences in the files do not match."

# Tokenize and compute BLEU scores with Smoothing function
bleu_scores = []
smoothie = SmoothingFunction().method4
for ref_sentence, cand_sentence in zip(reference_sentences, candidate_sentences):
    reference = [ref_sentence.strip().split()]
    candidate = cand_sentence.strip().split()
    score = sentence_bleu(reference, candidate, smoothing_function=smoothie)
    bleu_scores.append(score)

# Print BLEU scores
for i, score in enumerate(bleu_scores):
    print(f"Sentence {i+1}: BLEU Score = {score:.4f}")

# Calculate the average BLEU score
average_score = sum(bleu_scores) / len(bleu_scores)
print(f"Average BLEU Score: {average_score:.4f}")
