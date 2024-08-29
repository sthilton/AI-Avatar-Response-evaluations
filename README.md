# Evaluating Conversational AI with Custom Knowledge Banks

Welcome to the repository for evaluating conversational AI models with custom knowledge banks! This project provides tools and scripts to assess how effectively conversational AI systems can learn and respond using custom, domain-specific information. By comparing the AI-generated responses to pre-defined model answers, we aim to measure the accuracy and quality of the responses through various metrics like **F1 Score**, **BLEU**, and **BERT Score**.

Conversational AI systems, such as chatbots and virtual assistants, are increasingly being used in specialized domains where they must generate accurate and contextually appropriate responses based on a custom knowledge base. Evaluating how well these systems perform with domain-specific information is crucial for their development and deployment.

## Evaluation Metrics
### F1 Score
The F1 score is a harmonic mean of precision and recall, providing a balance between the two. It is particularly useful in scenarios where both false positives and false negatives are critical.

### BLEU (Bilingual Evaluation Understudy)
BLEU score measures the similarity between the AI-generated text and the reference text (model answer) by calculating n-gram overlaps. It is widely used in machine translation and text generation tasks.

### BERT Score
BERT score leverages the pre-trained BERT model to evaluate the semantic similarity between the AI response and the model answer. Unlike BLEU, which focuses on exact matches, BERT score considers the contextual meaning of the sentences.

**_Reference Literature:_**

[BLEU: a method for automatic evaluation of machine translation _Papineni et al._, 2002](https://doi.org/10.3115/1073083.1073135)

[BERTScore: Evaluating Text Generation with BERT _Zhang et al._, 2020](https://doi.org/10.48550/arXiv.1904.09675)




[![CC BY-NC 4.0][cc-by-nc-shield]][cc-by-nc]

This work is licensed under a
[Creative Commons Attribution-NonCommercial 4.0 International License][cc-by-nc].

[![CC BY-NC 4.0][cc-by-nc-image]][cc-by-nc]

[cc-by-nc]: https://creativecommons.org/licenses/by-nc/4.0/
[cc-by-nc-image]: https://licensebuttons.net/l/by-nc/4.0/88x31.png
[cc-by-nc-shield]: https://img.shields.io/badge/License-CC%20BY--NC%204.0-lightgrey.svg


This work is licensed under a Creative Commons Attribution-NonCommercial 4.0 International License.

CC BY-NC 4.0


**Author Attributions:**

Stephen Hilton

Mae Taylor
