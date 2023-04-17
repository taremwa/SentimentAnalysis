#Cleaning texxt steps:
# 1) Creating text files and extracting text from it
# 2) Convert the text to lowercase 
# 3) Remove punctuations eg .,!? ...


import string
from collections import Counter
import matplotlib.pyplot as plt

text = open('stevjobs.txt', encoding='utf-8').read()
#print(text)
lower_case = text.lower()
#print(lower_case)
#print(string.punctuation)

#Removing punctuations
cleaned_text = lower_case.translate(str.maketrans('','',string.punctuation))
#print(cleaned_text)

tokenized_words = cleaned_text.split()
#print(tokenized_words)

stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
              "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
              "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these",
              "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do",
              "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
              "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
              "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
              "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
              "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
              "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]

#tokenizing (removing stop words)
final_words = []
for word in tokenized_words:
    if word not in stop_words:
        final_words.append(word)
#print(final_words) 

#analysing the emotion in the file
emotion_list = []
with open('emotions.txt','r') as file:
    for line in file:
        clear_line = line.replace("\n", '').replace(",",'').replace("'",'').strip()
        #print(clear_line)
        word, emotion = clear_line.split(':')
        #print("Word:" + word + " " + "Emotion" + emotion)


#Check whether words from our text are in the emotion file
        if word in final_words:
            emotion_list.append(emotion)
print(emotion_list)

w = Counter(emotion_list)
print(w)

fig, ax1 = plt.subplots()
ax1.bar(w.keys(),w.values())
fig.autofmt_xdate()
plt.savefig('stevjobs_graph.png')
plt.show()