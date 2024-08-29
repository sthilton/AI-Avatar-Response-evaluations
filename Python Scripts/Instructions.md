# Instructions for how to use AI-Evaluation Python codes

## Setting up Python and installing Libraries

1. **Install Python:** To begin, ensure that you have Python installed on your machine. This project requires Python 3.6 or higher.
   If you don't have Python installed, you can download it from the official Python website: [Download Python](https://www.python.org/downloads/)
2. **Setting Up a Virtual Environment with PyCharm (Optional but Recommended):** Download instructions as well as manuals for setting up new Virtual Environments can be found [here](https://www.jetbrains.com/pycharm/).
3. **Install required libraries:** This project relies on several Python libraries for data processing, natural language processing, and evaluation metrics. Ensure the following libraries are installed;
   - pandas: Used for data manipulation and analysis, particularly for handling CSV files.
   - scikit-learn: Provides tools for machine learning, including functions to calculate precision, recall, and F1 score.
   - nltk: The Natural Language Toolkit, which includes utilities for text processing and evaluation, such as BLEU score calculation.
   - bert-score: A library for evaluating the similarity between sentences using the BERT model, which captures semantic meaning.
  
## Running the evaluations

1. **F1 Score Calculation:**
  This script compares the AI-generated answers with the model answers and calculates precision, recall, and F1 scores.

    **How to use:**
   
    - Create an excel file with two columns. Column one will be numbers for your answers, while column two contains a title 'reference_answers', or 'generated_answers', and your answers. **_Note:_** These column titles must match the code exactly or the script will not know which column contains the answers.
    - Ensure all answers are contained with one row (watch out for answers containing lists), and ensure the number of rows in your reference answers and generated answers match exactly.
    - Replace reference_csv_path and generated_csv_path in the code with the paths to your respective CSV files.
    - Run the script to print precision, recall, and F1 scores for each answer, along with the average F1 score.


3. **BLEU Score Calculation:**
This script computes the BLEU score for each pair of sentences from the model and generated answers.

    **How to use:**

    - Create a plain text file containing your answers. You do not need to number these answers nor add a title. All answers should be given on a single line. 
    **_Note:_** Once again, ensure that the number of lines in your model answers matches the number of lines in your generated answers, and watch for lists!
    - Save these .txt files in the same file directory as your Python script. Or, modify the script to include your file path.
    - Replace 'Model answers.txt' and 'Trained answers.txt' in the scipt with the name of your text files.
    - Run the script to print the BLEU score for each sentence and the average BLEU score.
    - Run the script to print precision, recall, and F1 scores for each answer, along with the average F1 score.


5. **BERTScore Calculation:**
This script evaluates the semantic similarity between the model and generated answers using BERT Score.

    **How to use:**
   
    - Where prompted in the code, add the file paths to the text files you created above.
    - Run the script to print the precision, recall, and F1 scores for each answer, along with the overall system-level BERTScore. 
