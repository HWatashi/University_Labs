import nltk
from nltk.corpus import gutenberg
from nltk.probability import FreqDist
import matplotlib.pyplot as plt
import string
from nltk.corpus import stopwords

nltk.download('punkt')
nltk.download('stopwords')

file_name = 'shakespeare-macbeth.txt'
macbeth_text = gutenberg.raw(file_name)

words = nltk.word_tokenize(macbeth_text)
num_words = len(words)
print("Кількість слів у тексті:", num_words)

word_freq = FreqDist(words)
top_words = word_freq.most_common(10)
print("10 найбільш вживаних слів у тексті:", top_words)

words, frequencies = zip(*top_words)
plt.figure(figsize=(10, 6))
plt.bar(words, frequencies)
plt.title('10 найбільш вживаних слів у тексті Shakespeare Macbeth')
plt.xlabel('Слова')
plt.ylabel('Частота')
plt.xticks(rotation=45)
plt.show()

words = nltk.word_tokenize(macbeth_text)

stop_words = set(stopwords.words('english'))
punctuation = set(string.punctuation)

additional_stop_words = ["'d", "'s", "macb", "macbeth"]

filtered_words = [
    word.lower()
    for word in words
    if word.lower() not in stop_words
    and word.lower() not in punctuation
    and word.lower() not in additional_stop_words
]

filtered_word_freq = FreqDist(filtered_words)
filtered_top_words = filtered_word_freq.most_common(10)
print("Зфільтровані слова та їх частота:", filtered_top_words)

if not filtered_top_words:
    print("Список порожній, проблема з фільтрацією")

plt.figure(figsize=(10, 6))
if filtered_top_words:
    filtered_words, filtered_frequencies = zip(*filtered_top_words)
    plt.bar(filtered_words, filtered_frequencies)
    plt.title('10 найбільш вживаних слів у фільтрованому тексті Shakespeare Macbeth')
    plt.xlabel('Слова')
    plt.ylabel('Частота')
    plt.xticks(rotation=45)
    plt.show()
else:
    print("Не вдалося побудувати діаграму, список порожній") 
