import string
from collections import Counter
#import nltk
#nltk.download('vader_lexicon')
#nltk.download('stopwords')
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt

text = open("read.txt", encoding="utf-8").read()

lower_case = text.lower()

cleaned_text = lower_case.translate(str.maketrans('','', string.punctuation))

tokenized_words = word_tokenize(cleaned_text, "english")

#print(tokenized_words)

#Removing stop words from the tokenized words list
final_words = []
for word in tokenized_words:
    if word not in stopwords.words('english'):
        final_words.append(word)
#print(final_words)

#analyzing the emotio in the text
emotion_list = []
with open('emotions.txt', 'r') as file:
    for line in file:
        clear_line = line.replace("\n",'').replace(",",'').replace("'",'').strip()
        word, emotion = clear_line.split(':')
        if word in final_words:
            emotion_list.append(emotion)

w = Counter(emotion_list)

#using nltk sentimentAnalyzer library to detect sentiment in the text
def sentiment_analyze(sentiment_text):
    score = SentimentIntensityAnalyzer().polarity_scores(sentiment_text)
    neg = score['neg']
    pos = score['pos']
    if neg > pos:
        print("Negative Sentiment")
    elif pos >neg:
        print("Postive Sentiment")
    else:
        print("Neitral Sentiment")
sentiment_analyze(cleaned_text)

fig, ax1 = plt.subplots()
ax1.bar(w.keys(),w.values())
fig.autofmt_xdate()
plt.savefig('nltk_graph.png')
plt.show()
