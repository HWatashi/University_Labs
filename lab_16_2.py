import nltk
from nltk.corpus import gutenberg
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer, PorterStemmer
from nltk.corpus import stopwords
import string

nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')

file_name = 'shakespeare-macbeth.txt'
macbeth_text = gutenberg.raw(file_name)

words = word_tokenize(macbeth_text)

lemmatizer = WordNetLemmatizer()
stemmer = PorterStemmer()

processed_words = []
for word in words:
    lemma = lemmatizer.lemmatize(word)
    stem = stemmer.stem(word)
    processed_words.append((word, lemma, stem))

stop_words = set(stopwords.words('english'))
punctuation = set(string.punctuation)
filtered_words = [word for word in processed_words if word[0] not in stop_words and word[0] not in punctuation]

filtered_first_100_words = filtered_words[:100]

output_file_name = 'processed_macbeth.txt'
with open(output_file_name, 'w', encoding='utf-8') as file:
    for word in filtered_first_100_words:
        file.write(f'{word[2]}\n')
