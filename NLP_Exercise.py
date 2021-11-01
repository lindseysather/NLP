# Create a wordcloud of the top 15 words that
# are the most recurring. Make sure to remove 
# all stop words. Use only noun words for this 
# analysis.To get a good idea of what the book 
# of John is about, it would be better to eliminate 
# additional stop words that are found in the 
# context of the Bible. Please eliminate these 
# additional words from your WordCloud:

#thy, ye, verily, thee, hath, say, thou, art, shall

from pathlib import Path
import imageio
from wordcloud import WordCloud
from textblob import TextBlob
import nltk
import pandas as pd

"-----------GET WORDS------------"

nltk.download("stopwords")
from nltk.corpus import stopwords
stops = stopwords.words("english")
more_stops = ["thy", "ye", "verily", "thee", "hath", "say", "thou", "art", "shall"]
stops += more_stops

blob = TextBlob(Path('book of John text.txt').read_text())

items = blob.word_counts.items()
#print(items)
clean_items = [i for i in items if i[0] not in stops]
#print(clean_items[:15])

#sorts by most common words
sorted_list = sorted(clean_items, key=itemgetter(1), reverse=True)

#uses sorted words to get top 15
top15 = sorted_list[:15]
#df = pd.DataFrame(top15, columns=["word", "count"])


"----------WORDCLOUD----------"

mask_image = imageio.imread("mask_circle.png")

wordcloud = WordCloud(colormap='Blues', mask=mask_image, background_color='white')

wordcloud = wordcloud.generate(top15)

wordcloud = wordcloud.to_file("John_WordCloud.png")

print("done")




