from textblob import TextBlob

text = "Today is a beautiful day. Tomorrow looks like bad weather."

blob = TextBlob(text)

print(blob.sentences)
print(blob.words)

#print(blob.tags)

#print(blob.noun_phrases)

#tells you how positive/negative words are and how subjective they are
#-1 to 1 (close to 1 is positive)
print(round(blob.sentiment,3))
print('Polarity:', round(blob.sentiment.polarity,3))
print(round('Subjectivity:', blob.sentiment.subjectivity,3))

sentences = blob.sentences

for sentence in sentences:
    print(sentence)
    print(round(sentence.sentiment.polarity, 3))



'''Different analyzer'''
from textblob.sentiments import NaiveBayesAnalyzer

blob = TextBlob(text, analyzer=NaiveBayesAnalyzer())

#gives overall classification (positive or negative)
print(blob.sentiment)

for sentence in blob.sentences:
    print(sentence.sentiment)

spanish = blob.translate(to='es')
chinese = blob.translate(to='zh')

print(spanish)

print(spanish.translate)

print(chinese.translate)



print()

