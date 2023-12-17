import os
import numpy as np
import matplotlib.pyplot as plt
from os import path
from PIL import Image
from wordcloud import WordCloud, STOPWORDS

# 'datasets/daily_self_gil.txt' 
FILE = 'datasets/self_appreciation_2023.txt'
MASK = 'images/masks/cloud.png'

# get data directory (using getcwd() is needed to support running example in generated IPython notebook)
d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()

# Read the whole text.
text = open(path.join(d, FILE)).read()

# read the mask image
image_mask = np.array(Image.open(path.join(d, MASK)))

stopwords = set(STOPWORDS)

# Customize my Wordcloud
stopwords.add('smile')
stopwords.add('legs')

wc = WordCloud(background_color="white", max_words=5000, mask=image_mask,
               stopwords=stopwords, contour_width=3, contour_color='steelblue')

# generate word cloud
wc.generate(text)

# store to file
wc.to_file(path.join(d, "images/gil_self.png"))

# show
plt.imshow(wc, interpolation='bilinear')
plt.axis("off")
plt.figure()
plt.imshow(image_mask, cmap=plt.cm.gray, interpolation='bilinear')
plt.axis("off")
plt.show()