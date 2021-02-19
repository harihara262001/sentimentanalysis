import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.sentiment.vader import SentimentIntensityAnalyzer

text = input("Enter input")

lower_case = text.lower()
cleaned_text = lower_case.translate(str.maketrans('','',string.punctuation))

tokenized_words = word_tokenize(cleaned_text,"english")

final_words = []
for word in tokenized_words:
    if word not in stopwords.words('english'):
        final_words.append(word)
v1=''
score = SentimentIntensityAnalyzer().polarity_scores(text)
neg = score['neg']
pos = score['pos']
if neg > pos:
    v1="neg"   #neg
elif pos > neg:
    v1="pos" 
else:
    v1="neut"   #neut

print(v1)


