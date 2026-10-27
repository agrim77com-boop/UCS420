import re
import nltk
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from nltk.stem import PorterStemmer, WordNetLemmatizer
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from textblob import TextBlob
from wordcloud import WordCloud

for resource in [
    "punkt", "punkt_tab", "stopwords", "wordnet", "omw-1.4"
]:
    nltk.download(resource, quiet=True)

STOP_WORDS = set(stopwords.words("english"))
print("Setup complete.")

#q1
paragraph = (
    "Football is my favorite sport because it combines skill, teamwork, and strategy. "
    "I enjoy watching players create chances through quick passes and intelligent movement. "
    "A good team communicates well and supports every player on the field. "
    "The final minutes of a close match are especially exciting because one moment can change everything. "
    "Playing football also improves fitness, discipline, and decision-making. "
    "For me, football is more than a game because it brings people together."
)

print("Original paragraph:\n", paragraph)

# 1. Convert to lowercase and remove punctuation using re.
clean_text = re.sub(r"[^a-zA-Z0-9\s]", "", paragraph.lower())
print("\nLowercase text without punctuation:\n", clean_text)

# 2. Tokenize into words and sentences.
word_tokens = word_tokenize(paragraph)
sentence_tokens = sent_tokenize(paragraph)
print("\nWord tokens:", word_tokens)
print("\nSentence tokens:")
for sentence in sentence_tokens:
    print("-", sentence)

# 3. Compare Python split() with NLTK word_tokenize().
split_tokens = paragraph.split()
nltk_tokens = word_tokenize(paragraph)
print("\nsplit() tokens:", split_tokens)
print("\nword_tokenize() tokens:", nltk_tokens)
print("\nComparison: split() separates on whitespace and may keep punctuation attached to words. "
      "word_tokenize() handles punctuation as separate tokens and uses language-aware tokenization.")

# 4. Remove stopwords.
tokens_lower = [w.lower() for w in word_tokenize(clean_text) if w.isalpha()]
filtered_tokens = [w for w in tokens_lower if w not in STOP_WORDS]
print("\nTokens after stopword removal:", filtered_tokens)

# 5. Word frequency distribution excluding stopwords.
frequency = FreqDist(filtered_tokens)
print("\nWord frequency distribution:")
for word, count in frequency.most_common():
    print(f"{word}: {count}")

frequency.plot(10, title="Q1: Most Common Words (Stopwords Removed)")
plt.show()

#q2
# 1. Extract alphabetic words using re.findall().
alphabetic_words = re.findall(r"\b[a-zA-Z]+\b", paragraph.lower())
print("Alphabetic words:", alphabetic_words)

# 2. Remove stopwords.
content_words = [w for w in alphabetic_words if w not in STOP_WORDS]
print("\nAfter stopword removal:", content_words)

# 3. Porter stemming and 4. WordNet lemmatization.
stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()
stemmed = [stemmer.stem(w) for w in content_words]
lemmatized = [lemmatizer.lemmatize(w) for w in content_words]

print("\nStemmed words:")
print(stemmed)
print("\nLemmatized words:")
print(lemmatized)

# Compare corresponding results.
print("\nComparison:")
for original, stem, lemma in zip(content_words, stemmed, lemmatized):
    print(f"{original:15} -> stem: {stem:12} | lemma: {lemma}")

print("\nInterpretation: Stemming mechanically removes word endings and may produce a non-word "
      "(for example, 'intelligent' can be reduced to 'intellig'). Lemmatization uses vocabulary "
      "and linguistic rules to return a dictionary form. Stemming is useful when speed and broad "
      "matching matter; lemmatization is preferable when readable, linguistically meaningful words matter.")

#q3
texts = [
    "The new smartphone has a bright screen and long battery life.",
    "The camera takes sharp photos, but the battery drains quickly.",
    "This laptop is fast, lightweight, and useful for programming."
]

print("Input texts:")
for i, text in enumerate(texts, start=1):
    print(f"Text {i}: {text}")

# 1. Bag of Words using CountVectorizer.
count_vectorizer = CountVectorizer(stop_words="english")
bow_matrix = count_vectorizer.fit_transform(texts)
print("\nBag of Words vocabulary:")
print(count_vectorizer.get_feature_names_out())
print("\nBag of Words matrix:")
print(bow_matrix.toarray())

# 2. TF-IDF scores.
tfidf_vectorizer = TfidfVectorizer(stop_words="english")
tfidf_matrix = tfidf_vectorizer.fit_transform(texts)
terms = tfidf_vectorizer.get_feature_names_out()
print("\nTF-IDF matrix (rounded):")
print(np.round(tfidf_matrix.toarray(), 3))

# 3. Top 3 keywords per text by TF-IDF score.
print("\nTop 3 TF-IDF keywords for each text:")
for i, row in enumerate(tfidf_matrix.toarray(), start=1):
    top_indices = row.argsort()[::-1][:3]
    keywords = [(terms[j], round(float(row[j]), 3)) for j in top_indices if row[j] > 0]
    print(f"Text {i}: {keywords}")

print("\nInterpretation: Bag of Words records how often terms appear. TF-IDF gives more weight "
      "to terms that are important in a particular text but less common across the collection.")

#q4
technology_a = (
    "Artificial intelligence helps computers learn patterns from data.\n"
    "It supports prediction, language processing, and image recognition.\n"
    "AI systems can improve decisions by identifying useful patterns.\n"
    "They are used in healthcare, education, and transportation."
)
technology_b = (
    "Blockchain stores records in linked blocks across a distributed network.\n"
    "It supports transparent transactions and tamper-resistant data storage.\n"
    "Blockchain can improve trust by allowing participants to verify records.\n"
    "It is used in finance, supply chains, and digital identity."
)

print("Technology A — Artificial Intelligence:\n", technology_a)
print("\nTechnology B — Blockchain:\n", technology_b)

def preprocess_for_similarity(text):
    text = re.sub(r"[^a-zA-Z\s]", " ", text.lower())
    tokens = word_tokenize(text)
    return [token for token in tokens if token.isalpha() and token not in STOP_WORDS]

tokens_a = preprocess_for_similarity(technology_a)
tokens_b = preprocess_for_similarity(technology_b)
set_a, set_b = set(tokens_a), set(tokens_b)

# a. Jaccard similarity.
jaccard = len(set_a & set_b) / len(set_a | set_b) if (set_a | set_b) else 0.0
print("\nPreprocessed tokens A:", tokens_a)
print("Preprocessed tokens B:", tokens_b)
print(f"Jaccard similarity: {jaccard:.3f}")

# b. Cosine similarity using TF-IDF.
tfidf_sim_vectorizer = TfidfVectorizer(stop_words="english")
tfidf_pair = tfidf_sim_vectorizer.fit_transform([technology_a, technology_b])
cosine = float(cosine_similarity(tfidf_pair[0:1], tfidf_pair[1:2])[0, 0])
print(f"Cosine similarity: {cosine:.3f}")

# c. Compare the metrics.
print("\nAnalysis:")
print("Jaccard compares the overlap between the unique words in both texts. "
      "TF-IDF cosine similarity compares the direction of weighted word vectors, so it accounts "
      "for how informative words are in this two-text collection. In this example, both metrics "
      "should indicate limited overlap because the technologies use mostly different vocabulary. "
      "Cosine similarity can be more informative when terms have different importance; Jaccard is "
      "simpler and easy to interpret when only set overlap matters.")

#q5
reviews = [
    "The headphones sound excellent and the battery lasts all day.",
    "I love the comfortable design and the clear audio quality.",
    "The product is fantastic and very easy to use.",
    "The sound is poor and the device stopped working quickly.",
    "Terrible battery life and disappointing customer support.",
    "The headphones are uncomfortable and the connection keeps dropping.",
    "The package arrived today. The box contains the headphones and a charging cable."
]

review_results = []
for review in reviews:
    polarity = TextBlob(review).sentiment.polarity
    subjectivity = TextBlob(review).sentiment.subjectivity
    if polarity > 0.1:
        label = "Positive"
    elif polarity < -0.1:
        label = "Negative"
    else:
        label = "Neutral"
    review_results.append({
        "review": review,
        "polarity": round(polarity, 3),
        "subjectivity": round(subjectivity, 3),
        "sentiment": label
    })

print("Review sentiment results:")
for item in review_results:
    print(f"\nReview: {item['review']}")
    print(f"Polarity: {item['polarity']}, Subjectivity: {item['subjectivity']}, "
          f"Classification: {item['sentiment']}")

# Word cloud from positive reviews only.
positive_reviews = [item["review"] for item in review_results if item["sentiment"] == "Positive"]
if positive_reviews:
    positive_text = " ".join(positive_reviews)
    cloud = WordCloud(width=900, height=450, background_color="white",
                      stopwords=STOP_WORDS, collocations=False).generate(positive_text)
    plt.figure(figsize=(12, 6))
    plt.imshow(cloud, interpolation="bilinear")
    plt.axis("off")
    plt.title("Word Cloud — Positive Reviews")
    plt.show()
else:
    print("No positive reviews were found, so a word cloud could not be generated.")

print("\nInterpretation: Polarity ranges from -1 (negative) to +1 (positive). "
      "Subjectivity ranges from 0 (more objective) to 1 (more subjective). "
      "The thresholds above are a simple rule for this assignment; sentiment tools can misread sarcasm or context.")

#q6
import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense

tf.random.set_seed(42)
np.random.seed(42)

training_text = (
    "Technology changes the way people learn and communicate. "
    "Students use digital tools to explore ideas and solve problems. "
    "A computer can process information quickly, but people provide goals and creativity. "
    "Good software should be useful, reliable, and easy to understand. "
    "Learning programming takes patience and regular practice. "
    "Small projects help learners connect theory with real applications. "
    "Data can reveal patterns and support better decisions. "
    "Responsible technology should protect privacy and treat people fairly. "
    "In the future, collaboration between people and intelligent systems may help solve complex challenges. "
    "Curiosity encourages us to keep learning and improving."
)
print("Training text word count:", len(training_text.split()))

# 1. Tokenize using Keras Tokenizer.
tokenizer = Tokenizer()
tokenizer.fit_on_texts([training_text])
total_words = len(tokenizer.word_index) + 1
token_list = tokenizer.texts_to_sequences([training_text])[0]
print("Vocabulary size:", total_words)
print("Token sequence:", token_list)

# 2. Create input sequences; predict the next word from preceding words.
input_sequences = []
for i in range(2, len(token_list) + 1):
    input_sequences.append(token_list[:i])

max_sequence_len = max(len(seq) for seq in input_sequences)
padded_sequences = pad_sequences(input_sequences, maxlen=max_sequence_len, padding="pre")
X = padded_sequences[:, :-1]
y = padded_sequences[:, -1]
y = tf.keras.utils.to_categorical(y, num_classes=total_words)

print("X shape:", X.shape)
print("y shape:", y.shape)

# 3. Build and train a small LSTM model.
model = Sequential([
    Embedding(input_dim=total_words, output_dim=32, input_length=max_sequence_len - 1),
    LSTM(64),
    Dense(total_words, activation="softmax")
])
model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])
model.summary()

# A small number of epochs keeps this assignment reasonably quick.
history = model.fit(X, y, epochs=100, verbose=0)
print("Training complete. Final loss:", round(float(history.history["loss"][-1]), 4))

# 4. Generate 2–3 lines starting from a seed phrase.
def generate_text(seed_text, next_words=30):
    generated = seed_text
    for _ in range(next_words):
        sequence = tokenizer.texts_to_sequences([generated])[0]
        sequence = pad_sequences([sequence], maxlen=max_sequence_len - 1, padding="pre")
        probabilities = model.predict(sequence, verbose=0)[0]
        # Greedy decoding: choose the most likely next word.
        predicted_index = int(np.argmax(probabilities))
        if predicted_index == 0:
            break
        output_word = next((word for word, index in tokenizer.word_index.items()
                            if index == predicted_index), "")
        if not output_word:
            break
        generated += " " + output_word
    return generated

seed = "students use"
generated = generate_text(seed, next_words=30)
print("\nSeed:", seed)
print("Generated text:\n", generated)
print("\nNote: The output depends on the training data and model randomness. A small corpus often causes repetition.")
