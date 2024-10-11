## FAQ Matching Application Documentation

This application matches user questions to a list of frequently asked questions (FAQs) about the TOEFL iBT test. It provides several different matching methods, each using different natural language processing (NLP) techniques to improve semantic similarity.

### Inputs

- **User Input:** A question related to the TOEFL iBT test entered by the user through the command line. 

### Outputs

The application provides four sets of top 10 matched FAQs, each using a different method:

1. **Lemmatized Features:** This method uses lemmatization to reduce words to their base form. For example, "running", "ran", and "runs" would all be reduced to "run". 

2. **Stemmed Features:** Similar to lemmatization, stemming also reduces words to their root form. However, stemming is a simpler process and may not always result in a valid word.

3. **Dependency Parsing:**  This method analyzes the grammatical structure of the user's question and each FAQ, comparing their syntactic relationships for similarity. 

4. **WordNet Similarity:** This method utilizes the WordNet lexical database to determine the semantic similarity between the user's question and each FAQ. It considers synonyms, hyponyms, and other relationships between words to calculate a similarity score.


Each output includes:

- **Matched FAQ:** The text of the FAQ that most closely matches the user's question.

- **Similarity Score:** A numerical representation of the semantic similarity between the user's question and the matched FAQ. 

- **Answer:** The answer to the matched FAQ. 

---

This application showcases a simple FAQ matching system that leverages basic NLP techniques to improve semantic matching. By comparing different methods, users can gain insights into the strengths and weaknesses of each approach.  