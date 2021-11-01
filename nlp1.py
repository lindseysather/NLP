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


#CLASS 10/20

from textblob import Word

index = Word('indes')

print(index.pluralize())

cacti = Word('cacti')
print(cacti.singularize())


#wordlist
animals = TextBlob('dog cat fish bird').words
print(animals.pluralize())


#spellcheck and correction
word = Word('theyr')

#gives you possible spelling corrections with percent confidence 
    #returns ('they', 0.57), ('their', 0.43)
print(word.spellcheck())

#corrects it with the most confident option
    #returns they 
print(word.correct())


# Normalization 

word1 = Word("studies")
word2 = Word('varieties')

#stem takes out stem (not very accurate: studi, varieti)
print(word1.stem())
print(word2.stem())

#lemmatize takes actual stem (singluar noun: study, variety)
print(word1.lemmatize())
print(word2.lemmatize())


# Definitions, Synonyms and Antonyms from WordNet

happy = Word('happy')

print(happy.definitions)

#set of synonyms
print(happy.synsets)

#gets list of words 
for s in happy.synsets:
    for l in s.lemmas():
        print(l.name)

synonym = happy.synsets[1].lemmas()[0].name()
print(synonym)

antonym = happy.synseets[0].lemmas()[0].antonyms()[0].name()
print(antonym)


print()

