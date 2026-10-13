import nltk
import matplotlib.pyplot as plt
from collections import Counter
from nltk.tokenize import word_tokenize
from nltk.util import ngrams
from textblob import TextBlob

nltk.download("punkt", quiet=True)
nltk.download("punkt_tab", quiet=True)

text = """
Natural Language Processing helps computers understand human language.
Natural language processing is used in chatbots, search engines, and recommendation systems.
Language processing makes text useful for machine learning.
"""

# Question 1
tokens = [word.lower() for word in word_tokenize(text) if word.isalpha()]
types = set(tokens)

print("Tokens:", tokens)
print("Total tokens:", len(tokens))
print("Types:", sorted(types))
print("Total types:", len(types))

# Question 2
word_frequencies = Counter(tokens)

print("Word frequencies:")
for word, frequency in word_frequencies.most_common():
    print(f"{word}: {frequency}")

# Question 3
ranked_words = word_frequencies.most_common()
ranks = list(range(1, len(ranked_words) + 1))
frequencies = [frequency for _, frequency in ranked_words]

print("Zipf's Law - Rank and Frequency:")
for rank, (word, frequency) in enumerate(ranked_words, start=1):
    print(f"Rank {rank}: {word} - {frequency}")

plt.figure(figsize=(8, 5))
plt.loglog(ranks, frequencies, marker="o", linestyle="-")
plt.xlabel("Word Rank (log scale)")
plt.ylabel("Word Frequency (log scale)")
plt.title("Zipf's Law")
plt.grid(True)
plt.tight_layout()
plt.show()

# Question 4
singular_word = TextBlob("cars")
plural_word = TextBlob("child")

print("Singular of cars:", singular_word.words.singularize()[0])
print("Plural of child:", plural_word.words.pluralize()[0])

# Question 5
spanish_text = TextBlob("Hola, ¿cómo estás?")

try:
    translated_text = spanish_text.translate(to="en")
    print("English translation:", translated_text)
except Exception as error:
    print("Translation could not be completed. Check your internet connection and TextBlob version.")
    print("Details:", error)

# Question 6
sentence_tokens = ["machine", "learning", "is", "very", "useful"]

unigrams = list(ngrams(sentence_tokens, 1))
bigrams = list(ngrams(sentence_tokens, 2))
trigrams = list(ngrams(sentence_tokens, 3))

print("Unigrams:", unigrams)
print("Bigrams:", bigrams)
print("Trigrams:", trigrams)
