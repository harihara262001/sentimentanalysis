from flask import Flask, redirect, url_for, render_template, request
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.sentiment.vader import SentimentIntensityAnalyzer


app = Flask(__name__)               


@app.route('/')
@app.route('/home')
def home():
    return render_template("index-2.html")

@app.route('/review',methods=['GET','POST'])   
def review():
    var1=''
    if request.method=="POST":
        var1=request.form['message']
    text=var1 #input here
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
        v1="negative"   #neg
    elif pos > neg:
        v1="positive"  #pos
    else:              
        v1="neutral"
    
    print(v1)

    return render_template("review.html")            

if __name__ == "__main__":
    app.run(debug=True)          


























