from pathlib import Path
import imageio
from wordcloud import WordCloud

#brings text into an object to manipulate
text = Path('RomeoAndJuliet.txt').read_text()

#change mask to heart
mask_image = imageio.imread("mask_heart.png")

#formatting of word cloud
wordcloud = WordCloud(colormap='prism', mask=mask_image, background_color='white')

#text for wordcloud
wordcloud = wordcloud.generate(text)

#create a file
wordcloud = wordcloud.to_file("RomeoAndJulietHeart.png")

print("done")